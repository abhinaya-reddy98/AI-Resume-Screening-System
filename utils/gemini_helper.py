import streamlit as st
import google.generativeai as genai


def get_ai_feedback(resume_text, job_description):

    api_key = st.secrets["GEMINI_API_KEY"]

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Senior AI Recruiter, ATS Expert, and Career Coach.

Analyze the following resume against the given job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide your response in the following format:

# Resume Strengths
- Mention key strengths

# Missing Skills
- Mention missing technical skills

# Resume Improvements
- Suggest specific improvements

# Recommended Projects
- Recommend projects based on missing skills

# ATS Optimization Tips
- Suggest how to improve ATS score

# Overall Evaluation
- Give a short evaluation out of 10
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"