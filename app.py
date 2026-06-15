import streamlit as st
from pypdf import PdfReader

from data.skills import SKILLS
from utils.skill_extractor import extract_skills
from utils.ats import calculate_ats_score
from utils.suggestions import generate_suggestions
from utils.career_advisor import generate_career_advice
from utils.gemini_helper import get_ai_feedback
from utils.report_generator import generate_report


# ---------------- SESSION STATE ---------------- #

if "gemini_feedback" not in st.session_state:
    st.session_state.gemini_feedback = ""

if "celebrated" not in st.session_state:
    st.session_state.celebrated = False


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #eef2ff 50%,
        #f8fafc 100%
    );
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #4338ca;
    margin-top: 20px;
    margin-bottom: 0px;
}

.sub-title {
    text-align: center;
    color: #64748b;
    font-size: 18px;
    margin-bottom: 10px;
}

.hero-card {
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );
    padding: 25px;
    border-radius: 20px;
    color: white;
    margin-bottom: 20px;
}

.footer {
    text-align:center;
    color:#64748b;
    margin-top:30px;
}

div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.9);
    border-radius: 18px;
    padding: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-title">
📄 AI Resume Screening System
</div>

<div class="sub-title">
ATS Analysis • Skill Matching • Career Guidance • Gemini AI
</div>
""",
unsafe_allow_html=True)

st.caption(
    "AI-Powered Resume Screening | ATS Optimization | Gemini Career Coach"
)

st.markdown("---")


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.markdown("""
# 🚀 Resume AI Pro

### Smart Resume Intelligence

Analyze resumes using:

✅ ATS Matching

✅ Skill Detection

✅ Career Guidance

✅ Gemini AI Coach

✅ Downloadable Reports
""")

    st.markdown("---")

    st.success(
        "Built by Abhinaya Reddy"
    )


# ---------------- INPUT SECTION ---------------- #

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(
        "💼 Paste Job Description",
        height=250
    )


# ---------------- MAIN LOGIC ---------------- #

if uploaded_file is not None:

    try:

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:

                resume_text += text + "\n"

    except Exception as e:

        st.error(
            f"Error reading PDF: {e}"
        )

        st.stop()

    st.success(
        "✅ Resume uploaded successfully!"
    )

    skills = extract_skills(
        resume_text
    )

    skills = list(
        set(skills)
    )

    jd_skills = []

    if job_description.strip():

        jd_text = job_description.lower()

        for skill in SKILLS:

            if skill in jd_text:

                jd_skills.append(skill)

    jd_skills = list(
        set(jd_skills)
    )

    score, matched_skills, missing_skills = (
        calculate_ats_score(
            skills,
            jd_skills
        )
    )

    advice = generate_career_advice(
        score,
        missing_skills
    )

    # ---------------- HERO CARD ---------------- #

    st.markdown(
        f"""
        <div class="hero-card">

        <h2>🎯 Resume Match Score</h2>

        <h1>{score:.0f}%</h1>

        <p>
        AI-powered ATS evaluation completed successfully
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- DASHBOARD ---------------- #

    st.markdown(
        "## 📊 Resume Dashboard"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🎯 ATS Score",
        f"{score:.0f}%"
    )

    c2.metric(
        "🛠 Skills Found",
        len(skills)
    )

    c3.metric(
        "✅ Matched",
        len(matched_skills)
    )

    c4.metric(
        "❌ Missing",
        len(missing_skills)
    )

    st.progress(
        min(max(int(score), 0), 100)
    )

    st.markdown(
        f"""
        <h2 style='text-align:center;color:#4338ca'>
        🎯 ATS Score: {score:.0f}%
        </h2>
        """,
        unsafe_allow_html=True
    )

    if score >= 80:

        if not st.session_state.celebrated:

            st.balloons()

            st.session_state.celebrated = True

        st.success(
            "Excellent Match! Resume is highly aligned with the job description."
        )

    elif score >= 60:

        st.warning(
            "Good Match! Some improvements can increase your ATS score."
        )

    else:

        st.error(
            "Low Match! Consider improving your skills and projects."
        )

    # ---------------- TABS ---------------- #

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🛠 Skills",
            "💡 Suggestions",
            "🚀 Career Advisor",
            "🤖 Gemini AI"
        ]
    )

    # ---------------- TAB 1 ---------------- #

    with tab1:

        col_a, col_b = st.columns(2)

        with col_a:

            st.subheader("✅ Matched Skills")

            if matched_skills:

                for skill in matched_skills:

                    st.success(
                        skill.title()
                    )

            else:

                st.info(
                    "No matched skills found."
                )

        with col_b:

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.error(
                        skill.title()
                    )

            else:

                st.success(
                    "No missing skills found."
                )

    # ---------------- TAB 2 ---------------- #

    with tab2:

        st.subheader(
            "💡 Resume Improvement Suggestions"
        )

        suggestions = generate_suggestions(
            missing_skills
        )

        if suggestions:

            for suggestion in suggestions:

                st.info(
                    suggestion
                )

        else:

            st.success(
                "Your resume already contains all required skills."
            )

    # ---------------- TAB 3 ---------------- #

    with tab3:

        st.subheader(
            "🚀 Career Advisor"
        )

        for item in advice:

            st.info(
                item
            )

    # ---------------- TAB 4 ---------------- #

    with tab4:

        st.subheader(
            "🤖 Gemini AI Analysis"
        )

        if st.button(
            "Generate AI Feedback",
            key="gemini_button"
        ):

            with st.spinner(
                "Gemini is analyzing your resume..."
            ):

                st.session_state.gemini_feedback = (
                    get_ai_feedback(
                        resume_text,
                        job_description
                    )
                )

        if st.session_state.gemini_feedback:

            st.markdown("---")

            with st.container(
                border=True
            ):

                with st.expander(
                    "📋 View Detailed AI Analysis",
                    expanded=True
                ):

                    st.markdown(
                        st.session_state.gemini_feedback
                    )

    # ---------------- RESUME PARSER ---------------- #

    with st.expander(
        "📄 Extracted Resume Content"
    ):

        st.text_area(
            "Resume Content",
            resume_text,
            height=350,
            disabled=True
        )

    # ---------------- REPORT DOWNLOAD ---------------- #

    report = generate_report(
        score,
        matched_skills,
        missing_skills,
        advice,
        st.session_state.gemini_feedback
    )

    st.download_button(
        label="📥 Download Complete Report",
        data=report,
        file_name="AI_Resume_Report.txt",
        mime="text/plain"
    )

    st.success(
        "Analysis complete. Download your report and review Gemini recommendations."
    )

    # ---------------- SIDEBAR STATS ---------------- #

    with st.sidebar:

        st.markdown("---")

        st.metric(
            "Current ATS",
            f"{score:.0f}%"
        )

        st.metric(
            "Skills Found",
            len(skills)
        )

        st.metric(
            "Matched Skills",
            len(matched_skills)
        )


# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    """
<div class="footer">
Developed by Abhinaya Reddy • AI Resume Screening System
</div>
""",
    unsafe_allow_html=True
)