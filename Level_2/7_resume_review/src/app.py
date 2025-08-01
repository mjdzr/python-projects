import streamlit as st
from PyPDF2 import PdfReader
import yaml

from llm_interface import call_llm
from prompts import (
    RESUME_YAML_SCHEMA,
    LLM_YAML_PARSE_PROMPT,
    RESUME_REVIEW_PROMPT,
    REVIEW_OUTPUT_SCHEMA,
    JOB_DESCRIPTION_REVIEW_PROMPT
)
from constants import EXAMPLE_JOB_DESCRIPTION

def extract_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        resume_text += text or ""
    return resume_text

def clean_yaml_code_block(yaml_str):
    """
    Removes markdown code fences from LLM output.
    """
    lines = yaml_str.strip().splitlines()
    # Remove leading code fence if present
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    # Remove trailing code fence if present
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)

def parse_yaml(yaml_str):
    return yaml.safe_load(clean_yaml_code_block(yaml_str))

st.set_page_config(page_title="Resume Reviewer", layout="wide")
st.title("Resume Reviewer and Editor")

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
        
        with st.spinner("Parsing resume using LLM..."):
            prompt_yaml = LLM_YAML_PARSE_PROMPT.format(resume_text=resume_text, resume_schema=RESUME_YAML_SCHEMA)
            response_yaml = call_llm(prompt_yaml)
            parsed_resume = parse_yaml(response_yaml)
        
        if uploaded_jd is not None:
            job_description = uploaded_jd.read().decode("utf-8")
        else:
            job_description = EXAMPLE_JOB_DESCRIPTION

        with st.spinner("Reviewing your resume..."):
            review_prompt = RESUME_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            review_response = call_llm(review_prompt)
            review_dict = parse_yaml(review_response)

        st.success("Analysis complete!")
        
        # Section navigation
        all_sections = list(parsed_resume.keys())
        section = st.selectbox("Choose section to review:", all_sections, index=0)

        left, right = st.columns(2)
        with left:
            st.markdown(f"### Original: {section}")
            st.code(yaml.dump({section: parsed_resume.get(section, None)}, sort_keys=False), language="yaml")
        with right:
            st.markdown(f"### Suggestions / Fixes: {section}")
            if review_dict and section in review_dict and review_dict[section]:
                st.code(yaml.dump({section: review_dict[section]}, sort_keys=False), language="yaml")
            else:
                st.info("No fixes or suggestions for this section.")

st.info("Navigate sections using the dropdown to see the original and LLM-suggested fixes. Upload a job description for even more targeted feedback!")
