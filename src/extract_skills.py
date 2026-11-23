import re

SKILLS = [
    "python",
    "java",
    "c",
    "sql",
    "machine learning",
    "data structures",
    "pandas",
    "numpy",
    "html",
    "css",
    "excel",
    "data analysis",
    "mysql"
]


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill == "sql":
           pattern = r'(?<![a-z0-9])sql(?![a-z0-9])'
        else:
           pattern = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills