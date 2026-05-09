import streamlit as st
import pdfplumber

# Sidebar
st.sidebar.title("About Project")

st.sidebar.info(
    "This AI system analyzes resumes "
    "and matches skills with job descriptions."
)

# Title
st.title("📄 AI Resume Screening System")
st.write("Upload resume and check candidate suitability")

# Read Job Description
with open("jd.txt", "r") as file:
    jd_skills = file.read().lower().split()

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    # Extract text from PDF
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    resume_text = text.lower()

    # Skill Matching
    matched_skills = []

    for skill in jd_skills:
        if skill in resume_text:
            matched_skills.append(skill)

    # Match Percentage
    match_percent = (
        len(matched_skills) / len(jd_skills)
    ) * 100


    # Display Match Score
    st.subheader("Resume Match Score")

    st.progress(int(match_percent))

    st.write(f"### {match_percent:.2f}% Match")

    # Result
    if match_percent >= 60:
        st.success("Candidate Selected")
    else:
        st.error("Candidate Not Selected")