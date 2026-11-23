from src.generate_report import generate_report
from src.rank_candidates import rank_candidates
from src.match_resume import match_resume
from src.extract_skills import extract_skills
from src.clean_text import clean_text
print("===================================")
print(" AUTOMATED RESUME SCREENING TOOL")
print("===================================")

print("Project setup completed successfully!")
print("Ready to start building the application.")

import os
from src.extract_text import extract_text

resume_folder = "resumes"
job_file = "data/job_description.txt"

with open(job_file, "r", encoding="utf-8") as file:
    job_description = file.read()

required_skills = extract_skills(clean_text(job_description))

print("\nREQUIRED JOB SKILLS:")
print(required_skills)
candidates = []

for filename in os.listdir(resume_folder):

    
    file_path = os.path.join(resume_folder, filename)

    if os.path.isfile(file_path):

        print("\n===================================")
        print("RESUME:", filename)
        print("===================================")

        resume_text = extract_text(file_path)

        cleaned_text = clean_text(resume_text)

        skills = extract_skills(cleaned_text)
        result = match_resume(skills, required_skills)
        candidates.append({
          "candidate_name": filename,
          "match_percentage": result["match_percentage"],
          "matched_skills": result["matched_skills"],
          "missing_skills": result["missing_skills"]
        })

        print("\nMATCHED SKILLS:")
        print(result["matched_skills"])

        print("\nMISSING SKILLS:")
        print(result["missing_skills"])

        print("\nMATCHING PERCENTAGE:")
        print(result["match_percentage"], "%")

        print("\nEXTRACTED SKILLS:")
        print(skills)
        print("\nCLEANED RESUME:")
        print(cleaned_text)
print("\n========== CANDIDATE RANKING ==========")

ranked_candidates = rank_candidates(candidates)

for rank, candidate in enumerate(ranked_candidates, start=1):

    print(f"\nRank: {rank}")
    print("Candidate:", candidate["candidate_name"])
    print("Matching Score:", candidate["match_percentage"], "%")        
generate_report(ranked_candidates)