import streamlit as st
from PyPDF2 import PdfReader
from llm_interface import call_llm
from prompts import RESUME_YAML_SCHEMA, LLM_YAML_PARSE_PROMPT, RESUME_REVIEW_PROMPT, REVIEW_OUTPUT_SCHEMA, JOB_DESCRIPTION_REVIEW_PROMPT
from constants import EXAMPLE_JOB_DESCRIPTION

def extract_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        resume_text += text or ""
    return resume_text

st.set_page_config(page_title="Resume Reviewer", layout="wide")
st.title("Resume Reviewer and Editor")

with st.form("resume_form"):
    uploaded_pdf = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    uploaded_jd = st.file_uploader("Optionally upload a job description (TXT)", type=["txt"])
    submit_btn = st.form_submit_button("Analyze Resume")

if submit_btn:
    if uploaded_pdf is None:
        st.error("Please upload a resume PDF to continue.")
    else:
        # Extract resume text
        with st.spinner("Extracting text from PDF..."):
            resume_text = extract_from_pdf(uploaded_pdf)

        # Parse CV using LLM to YAML schema
        with st.spinner("Parsing resume using LLM..."):
            prompt_yaml = LLM_YAML_PARSE_PROMPT.format(resume_text=resume_text, resume_schema=RESUME_YAML_SCHEMA)
            response_yaml = call_llm(prompt_yaml)

        st.subheader("Extracted Resume Data (YAML)")
        st.code(response_yaml, language="yaml")

        # Review resume with/without job description
        if uploaded_jd:
            job_description = uploaded_jd.read().decode("utf-8")
        else:
            job_description = EXAMPLE_JOB_DESCRIPTION

        with st.spinner("Reviewing your resume..."):
            # Review fixes
            review_prompt = RESUME_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            review_response = call_llm(review_prompt)
            st.subheader("Resume Section Fixes & Suggestions")
            st.code(review_response, language="yaml")

            # Review based on job description
            job_review_prompt = JOB_DESCRIPTION_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                job_description=job_description,
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            jd_review_response = call_llm(job_review_prompt)
            st.subheader("Resume Fixes Based on Job Description")
            st.code(jd_review_response, language="yaml")

        st.success("Analysis complete!")

st.info("This tool extracts your resume, parses its structure, and makes improvement suggestions, optionally in the context of a job description.")
