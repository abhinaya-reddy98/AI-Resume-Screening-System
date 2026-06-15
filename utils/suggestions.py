def generate_suggestions(missing_skills):

    suggestions = []

    skill_suggestions = {
        "tensorflow": "Build a Deep Learning project using TensorFlow.",
        "pytorch": "Learn PyTorch and create a CNN-based project.",
        "aws": "Learn AWS and deploy an ML application.",
        "docker": "Learn Docker to containerize ML applications.",
        "streamlit": "Build interactive AI dashboards using Streamlit.",
        "github": "Showcase projects on GitHub with proper documentation.",
        "power bi": "Create business dashboards using Power BI.",
        "tableau": "Improve data visualization skills using Tableau."
    }

    for skill in missing_skills:

        if skill in skill_suggestions:

            suggestions.append(
                skill_suggestions[skill]
            )

        else:

            suggestions.append(
                f"Consider learning or highlighting {skill.title()} in your resume."
            )

    return suggestions