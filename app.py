import streamlit as st
import pandas as pd

from src.extract_text import extract_text
from src.clean_text import clean_text
from src.extract_skills import extract_skills
from src.match_resume import match_resume
from src.rank_candidates import rank_candidates

st.title("Automated Resume Screening Tool")

st.write("Welcome to the Resume Screening Application!")

st.info("Upload resumes to analyze their skills and matching scores.")

# Resume Upload
uploaded_files = st.file_uploader(
    "Upload Candidate Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success("Resumes uploaded successfully!")

    for file in uploaded_files:
        st.write(file.name)

# Job Description
st.subheader("Job Description")

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    default_description = file.read()

job_description = st.text_area(
    "Enter Job Description",
    value=default_description,
    height=200
)
st.divider()

if st.button("Analyze Resumes"):

    if uploaded_files:

        required_skills = extract_skills(clean_text(job_description))

        candidates = []

        for uploaded_file in uploaded_files:

            import os
            import tempfile

            suffix = os.path.splitext(uploaded_file.name)[1]

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            )

            temp_file.write(uploaded_file.getbuffer())
            temp_file.close()

            resume_text = extract_text(temp_file.name)

            os.remove(temp_file.name)

            cleaned_text = clean_text(resume_text)

            skills = extract_skills(cleaned_text)

            result = match_resume(skills, required_skills)

            candidates.append({
              "candidate_name": uploaded_file.name,
              "match_percentage": result["match_percentage"],
              "matched_skills": result["matched_skills"],
              "missing_skills": result["missing_skills"]
           })

        ranked_candidates = rank_candidates(candidates)
        st.subheader("Dashboard Overview")

        total_candidates = len(ranked_candidates)

        average_score = sum(
         candidate["match_percentage"]
         for candidate in ranked_candidates
         ) / total_candidates

        highest_score = ranked_candidates[0]["match_percentage"]

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Candidates", total_candidates)

        col2.metric("Average Match", f"{average_score:.2f}%")

        col3.metric("Highest Match", f"{highest_score:.2f}%")

        st.success("Resume analysis completed!")

        st.subheader("Candidate Ranking")
        st.subheader("Candidate Match Comparison")

        chart_data = pd.DataFrame({
         "Candidate": [
          candidate["candidate_name"]
          for candidate in ranked_candidates
          ],
         "Match Score": [
          candidate["match_percentage"]
          for candidate in ranked_candidates
          ]
        })

        st.bar_chart(
         chart_data,
         x="Candidate",
         y="Match Score"
        )

        st.dataframe(
         ranked_candidates,
         column_config={
         "candidate_name": "Candidate Name",
         "match_percentage": st.column_config.NumberColumn(
            "Match Score (%)",
            format="%.2f%%"
         ),
         "matched_skills": "Matched Skills",
         "missing_skills": "Missing Skills"
       },
        use_container_width=True
        )
        st.subheader("Candidate Details")

        for candidate in ranked_candidates:

          with st.expander(
          f"{candidate['candidate_name']} - {candidate['match_percentage']}% Match"
          ):

                        st.write("**Matching Score:**", candidate["match_percentage"], "%")

                        st.write("**Matched Skills:**")
                        st.write(", ".join(candidate["matched_skills"]))

                        st.write("**Missing Skills:**")
                        st.write(", ".join(candidate["missing_skills"]))
        results_df = pd.DataFrame(ranked_candidates)

        csv_data = results_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Results as CSV",
            data=csv_data,
            file_name="candidate_ranking.csv",
            mime="text/csv"
        )

    else:
        st.warning("Please upload at least one resume.")