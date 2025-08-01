import streamlit as st
import yaml
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

def yaml_to_dict(yaml_str):
    return yaml.safe_load(yaml_str)

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

        # Parse YAML to dict for easy access
        parsed_resume = yaml_to_dict(response_yaml)

        if uploaded_jd:
            job_description = uploaded_jd.read().decode("utf-8")
        else:
            job_description = EXAMPLE_JOB_DESCRIPTION

        with st.spinner("Reviewing your resume..."):
            review_prompt = RESUME_REVIEW_PROMPT.format(
                resume_data=response_yaml, 
                review_output_schema=REVIEW_OUTPUT_SCHEMA)
            review_response = call_llm(review_prompt)
            # Parse review response YAML to dict
            review_dict = yaml_to_dict(review_response)
        
        st.success("Analysis complete!")

        # Select section to display
        all_sections = list(parsed_resume.keys())
        section = st.selectbox("Choose section to review:", all_sections)

        # Retrieve original and revised info for given section
        original_section = parsed_resume.get(section, "Not found")
        revised_section = review_dict.get(section, "No suggestions for this section.")

        # Show side-by-side
        left, right = st.columns(2)
        with left:
            st.markdown("### Original")
            st.code(yaml.dump({section: original_section}), language="yaml")
        with right:
            st.markdown("### Suggestions / Fixes")
            st.code(yaml.dump({section: revised_section}), language="yaml")

st.info("Navigate sections using the dropdown to see original and LLM-suggested fixes. Upload a job description for more targeted feedback.")
