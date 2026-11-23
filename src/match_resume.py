def match_resume(candidate_skills, required_skills):

    candidate_skills = set(candidate_skills)
    required_skills = set(required_skills)

    matched_skills = candidate_skills.intersection(required_skills)

    missing_skills = required_skills - candidate_skills

    if len(required_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100

    return {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": round(match_percentage, 2)
    }