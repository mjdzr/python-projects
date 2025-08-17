import re

import streamlit as st
import yaml
from streamlit_extras.stylable_container import stylable_container

from utils.llm import call_llm
from prompts import (JOB_DESCRIPTION_REVIEW_PROMPT, LLM_YAML_PARSE_PROMPT,
                     RESUME_REVIEW_PROMPT, RESUME_YAML_SCHEMA,
                     REVIEW_OUTPUT_SCHEMA)
from utils.pdf import extract_from_pdf
from utils.yaml import parse_yaml

st.set_page_config(page_title="Resume Reviewer", layout="wide")
st.markdown("<h1 style='text-align: center; color: darkgreen;'>Resume Reviewer and Editor</h1>", unsafe_allow_html=True)

st.markdown("1. Upload file(s)")
with st.expander("File Upload", expanded=True):
    uploaded_pdf = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="pdf_upload")
    uploaded_jd = st.file_uploader("Optionally upload a job description (TXT)", type=["txt"], key="jd_upload")
    submit_btn = st.button("Analyze Resume")

st.title("2. Resume Analysis Results")
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

        with st.spinner("Reviewing your resume..."):
            # If job description is uploaded, use 
            if uploaded_jd is not None:
                job_description = uploaded_jd.read().decode("utf-8")
                review_prompt = JOB_DESCRIPTION_REVIEW_PROMPT.format(
                    resume_data=response_yaml,
                    job_description=job_description,
                    review_output_schema=REVIEW_OUTPUT_SCHEMA
                )
            else:
                review_prompt = RESUME_REVIEW_PROMPT.format(
                    resume_data=response_yaml,
                    review_output_schema=REVIEW_OUTPUT_SCHEMA
                )
            review_response = call_llm(review_prompt)
            review_dict = parse_yaml(review_response)
            st.session_state.review_dict = review_dict

        st.success("Analysis complete!")

# Show section navigation and comparison only if data exists
if st.session_state.parsed_resume is not None and st.session_state.all_sections:
    idx = st.session_state.section_index
    all_sections = st.session_state.all_sections

    # Navigation row
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        if st.button("← Previous", disabled=idx == 0):
            if st.session_state.section_index > 0:
                st.session_state.section_index -= 1
                st.rerun()

    with col2:
        st.markdown(
            f"<div style='text-align: center; font-size: 1.2em;'>Section {idx+1} of {len(all_sections)}</div>",
            unsafe_allow_html=True
        )

    with col3:
        with stylable_container(
            key="right_aligned_button_container",
            css_styles="""
                button {
                    float: right;
                }
            """
        ):
            if st.button("Next →", disabled=idx == len(all_sections) - 1):
                if st.session_state.section_index < len(all_sections) - 1:
                    st.session_state.section_index += 1
                    st.rerun()


    # Section display
    # Add a section on top of everything that shows the impact level 
    section = all_sections[idx]

    # Access the impact level for the current section from the review_dict
    impact_level = None
    review_dict = st.session_state.review_dict
    if review_dict and section in review_dict and review_dict[section]:
        impact_level = review_dict[section].get('impact_level', 'No Impact Level')

    # Display the impact level
    if impact_level:
        if impact_level == "Low":
            st.info(f"Impact Level: {impact_level}")
        elif impact_level == "Medium":
            st.warning(f"Impact Level: {impact_level}")
        elif impact_level == "High":
            st.error(f"Impact Level: {impact_level}")

    left, right = st.columns(2)
    with left:
        st.info(re.sub(r'[^A-Za-z/:]+', ' ', f"### Original: {section}").title())
        st.code(
            yaml.dump({section: st.session_state.parsed_resume.get(section, None)}, sort_keys=False),
            language="yaml"
        )
    with right:
        st.success(re.sub(r'[^A-Za-z/:]+', ' ', f"### Suggestions / Fixes: {section}").title())
        review_dict = st.session_state.review_dict
        if review_dict and section in review_dict and review_dict[section]:
            st.code(yaml.dump({section: review_dict[section]}, sort_keys=False), language="yaml")
        else:
            st.info("No fixes or suggestions for this section.")

    st.write(f"**Section {idx+1} of {len(all_sections)}**")

st.info("Use the Previous and Next buttons to navigate through your CV sections and see original vs. LLM-suggested fixes.")
