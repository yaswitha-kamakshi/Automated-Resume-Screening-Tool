
# 🚀 Automated Resume Screening Tool

An automated resume screening application developed using Python and Streamlit. It analyzes candidate resumes, extracts relevant skills, calculates matching scores based on job requirements, and ranks candidates accordingly.

## 📌 Project Overview

The Automated Resume Screening Tool simplifies the initial resume screening process by identifying skills from uploaded resumes and comparing them with the required skills mentioned in a job description.

It provides an interactive dashboard to view candidate rankings, matching scores, matched skills, and missing skills.

## ✨ Features

- 📄 Upload multiple resumes.
- Supports PDF, DOCX, and TXT formats.
- Extract text from resumes automatically.
- Clean and preprocess resume text.
- Extract relevant technical skills.
- Match candidate skills with job requirements.
- Calculate resume matching percentages.
- Rank candidates based on matching scores.
- Display matched and missing skills.
- Interactive dashboard with candidate statistics.
- Visual candidate comparison using bar charts.
- Download candidate results as CSV.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Data handling and CSV export |
| NumPy | Numerical computing |
| PDFPlumber | PDF text extraction |
| Python-docx | DOCX text extraction |
| Scikit-learn | Machine learning library |

## 📂 Project Structure

```text
Automated-Resume-Screening-Tool/
│
├── data/
│   └── job_description.txt
│
├── resumes/
│   ├── candidate1.txt
│   ├── candidate2.txt
│   └── candidate3.txt
│
├── src/
│   ├── extract_text.py
│   ├── clean_text.py
│   ├── extract_skills.py
│   ├── match_resume.py
│   ├── rank_candidates.py
│   └── generate_report.py
│
├── outputs/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Automated-Resume-Screening-Tool.git
```

### 2. Navigate to the Project Folder

```bash
cd Automated-Resume-Screening-Tool
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🔍 How It Works

1. Upload candidate resumes in PDF, DOCX, or TXT format.
2. Enter or modify the job description.
3. Extract text from uploaded resumes.
4. Clean and preprocess the extracted text.
5. Identify relevant skills.
6. Compare candidate skills with job requirements.
7. Calculate matching percentages.
8. Rank candidates based on their matching scores.
9. View results through an interactive dashboard.
10. Download candidate rankings as a CSV file.

## 📊 Matching Score Calculation

The application calculates matching percentages based on the number of required skills found in a candidate's resume.

**Formula:**

Matching Percentage = (Number of Matched Required Skills / Total Required Skills) × 100

The score represents skill overlap only, not the candidate's overall suitability.

## 📸 Project Screenshots

### 1. Main Application
![Main Application](screenshots/main-app.png)

### 2. Resume Analysis Results
![Analysis Results](screenshots/analysis-results.png)

### 3. Dashboard and Candidate Ranking
![Dashboard](screenshots/dashboard.png)

### 4. GitHub Repository
![GitHub Repository](screenshots/github-repository.png)

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming.
- File handling and text extraction.
- Text preprocessing.
- Regular expressions.
- Skill extraction and matching.
- Data processing using Pandas.
- Building interactive applications using Streamlit.
- Creating data visualizations.
- Git and GitHub.

## 🔮 Future Enhancements

- Advanced NLP-based resume analysis.
- Semantic similarity between resumes and job descriptions.
- Improved skill extraction.
- Candidate filtering and search.
- More detailed candidate reports.

## ⚠️ Disclaimer

This project is developed for educational purposes. Matching scores are based on predefined skill matching and should only support human review. They should not be used as the sole basis for recruitment decisions.

## 👩‍💻 Author

**Yaswitha Kamakshi V.**

B.Tech – Computer Science and Engineering

GitHub: https://github.com/yaswitha-kamakshi

LinkedIn: https://www.linkedin.com/in/yaswitha-kamakshi-292b5242b/

---

⭐ If you find this project interesting, feel free to explore the repository!
