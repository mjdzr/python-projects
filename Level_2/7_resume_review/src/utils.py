from PyPDF2 import PdfReader
import yaml

def extract_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        resume_text += text or ""
    return resume_text

def clean_yaml_code_block(yaml_str):
    lines = yaml_str.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)

def parse_yaml(yaml_str):
    return yaml.safe_load(clean_yaml_code_block(yaml_str))