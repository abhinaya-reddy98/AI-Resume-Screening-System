def generate_career_advice(score, missing_skills):

    advice = []

    if score >= 85:

        advice.append(
            "Excellent profile for AI and Data Science internships."
        )

        advice.append(
            "You are already highly aligned with most AI internship requirements."
        )

    elif score >= 70:

        advice.append(
            "Strong profile with good internship potential."
        )

        advice.append(
            "Adding a few industry-relevant skills can significantly improve your profile."
        )

    elif score >= 50:

        advice.append(
            "You have a solid foundation but need stronger projects and deployment skills."
        )

    else:

        advice.append(
            "Focus on improving both technical skills and practical projects."
        )

    if "tensorflow" in missing_skills:

        advice.append(
            "Build at least one Deep Learning project using TensorFlow."
        )

    if "pytorch" in missing_skills:

        advice.append(
            "Learn PyTorch and implement a CNN-based project."
        )

    if "aws" in missing_skills:

        advice.append(
            "Gain cloud deployment experience using AWS."
        )

    if "docker" in missing_skills:

        advice.append(
            "Learn Docker to containerize AI applications."
        )

    if "streamlit" in missing_skills:

        advice.append(
            "Build interactive AI dashboards using Streamlit."
        )

    advice.append(
        "Recommended Project: Medical Image Classification using CNN."
    )

    advice.append(
        "Recommended Project: End-to-End ML Deployment using AWS and Docker."
    )

    return advice