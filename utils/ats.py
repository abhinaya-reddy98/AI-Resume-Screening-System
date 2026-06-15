def calculate_ats_score(resume_skills, jd_skills):

    matched_skills = []

    missing_skills = []

    for skill in jd_skills:

        if skill in resume_skills:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    if len(jd_skills) == 0:

        score = 0

    else:

        score = round(
            (len(matched_skills) / len(jd_skills)) * 100,
            2
        )

    return score, matched_skills, missing_skills