import streamlit as st
from PyPDF2 import PdfReader

from constants import EXAMPLE_JOB_DESCRIPTION
from llm_interface import call_llm
from prompts import (JOB_DESCRIPTION_REVIEW_PROMPT, LLM_YAML_PARSE_PROMPT,
                     RESUME_REVIEW_PROMPT, RESUME_YAML_SCHEMA,
                     REVIEW_OUTPUT_SCHEMA)


def extract_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        resume_text += text or ""
    return resume_text

st.set_page_config(page_title="Resume Reviewer", layout="wide")
st.title("Resume Reviewer and Editor")

# --- Sidebar for inputs ---
with st.sidebar:
    st.header("Upload")
    uploaded_pdf = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    uploaded_jd = st.file_uploader("Optionally upload a job description (TXT)", type=["txt"])
    submit_btn = st.button("Analyze Resume")

if submit_btn:
    if uploaded_pdf is None:
        st.error("Please upload a resume PDF to continue.")
    else:
        with st.spinner("Extracting text from PDF..."):
            resume_text = extract_from_pdf(uploaded_pdf)
        
        # Parse CV using LLM to YAML schema
        with st.spinner("Parsing resume using LLM..."):
            prompt_yaml = LLM_YAML_PARSE_PROMPT.format(resume_text=resume_text, resume_schema=RESUME_YAML_SCHEMA)
            response_yaml = call_llm(prompt_yaml)

        # Optionally use job description
        if uploaded_jd is not None:
            job_description = uploaded_jd.read().decode("utf-8")
        else:
            job_description = EXAMPLE_JOB_DESCRIPTION

        with st.spinner("Reviewing your resume..."):
            # Resume review
            review_prompt = RESUME_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            review_response = call_llm(review_prompt)
            
            # JD-based review
            job_review_prompt = JOB_DESCRIPTION_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                job_description=job_description,
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            jd_review_response = call_llm(job_review_prompt)
        
        st.success("Analysis complete!")

        # --- Main content with expanders ---
        with st.expander("Show Extracted Resume Data (YAML)", expanded=False):
            st.code(response_yaml, language="yaml")

        with st.expander("Show Resume Section Fixes & Suggestions", expanded=False):
            st.code(review_response, language="yaml")

        with st.expander("Show Resume Fixes Based on Job Description", expanded=False):
            st.code(jd_review_response, language="yaml")

st.info("This tool extracts your resume, parses its structure, and makes improvement suggestions, optionally in the context of a job description.")
