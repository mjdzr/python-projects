import streamlit as st
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
from utils import extract_from_pdf, parse_yaml

st.set_page_config(page_title="Resume Reviewer", layout="wide")
st.title("Resume Reviewer and Editor")

with st.sidebar:
    st.header("Upload")
    uploaded_pdf = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="pdf_upload")
    uploaded_jd = st.file_uploader("Optionally upload a job description (TXT)", type=["txt"], key="jd_upload")
    submit_btn = st.button("Analyze Resume")

# Initialize session state keys
if "parsed_resume" not in st.session_state:
    st.session_state.parsed_resume = None
if "review_dict" not in st.session_state:
    st.session_state.review_dict = None
if "all_sections" not in st.session_state:
    st.session_state.all_sections = []
if "section_index" not in st.session_state:
    st.session_state.section_index = 0

if submit_btn:
    if uploaded_pdf is None:
        st.error("Please upload a resume PDF to continue.")
    else:
        with st.spinner("Extracting text from PDF..."):
            resume_text = extract_from_pdf(uploaded_pdf)
        
        with st.spinner("Parsing resume using LLM..."):
            prompt_yaml = LLM_YAML_PARSE_PROMPT.format(
                resume_text=resume_text, 
                resume_schema=RESUME_YAML_SCHEMA
            )
            response_yaml = call_llm(prompt_yaml)
            parsed_resume = parse_yaml(response_yaml)
            st.session_state.parsed_resume = parsed_resume
            st.session_state.all_sections = list(parsed_resume.keys())
            st.session_state.section_index = 0  # reset navigation index
        
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
            st.session_state.review_dict = review_dict

        st.success("Analysis complete!")

# Show section navigation and comparison only if data exists
if st.session_state.parsed_resume is not None and st.session_state.all_sections:
    idx = st.session_state.section_index
    all_sections = st.session_state.all_sections

    # Navigation row
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("Previous", disabled=idx == 0):
            if st.session_state.section_index > 0:
                st.session_state.section_index -= 1
                st.rerun()
    with col3:
        if st.button("Next", disabled=idx == len(all_sections) - 1):
            if st.session_state.section_index < len(all_sections) - 1:
                st.session_state.section_index += 1
                st.rerun()

    # Section display
    section = all_sections[idx]
    left, right = st.columns(2)
    with left:
        st.markdown(f"### Original: {section}")
        st.code(
            yaml.dump({section: st.session_state.parsed_resume.get(section, None)}, sort_keys=False),
            language="yaml"
        )
    with right:
        st.markdown(f"### Suggestions / Fixes: {section}")
        review_dict = st.session_state.review_dict
        if review_dict and section in review_dict and review_dict[section]:
            st.code(yaml.dump({section: review_dict[section]}, sort_keys=False), language="yaml")
        else:
            st.info("No fixes or suggestions for this section.")

    st.write(f"**Section {idx+1} of {len(all_sections)}**")

st.info("Use the Previous and Next buttons to navigate through your CV sections and see original vs. LLM-suggested fixes.")
