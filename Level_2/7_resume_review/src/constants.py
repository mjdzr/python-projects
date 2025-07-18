RESUME_SCHEMA = """
{
  "personal_info": {
    "full_name": "",
    "address": {
      "street": "",
      "city": "",
      "state": "",
      "zip": "",
      "country": ""
    },
    "phone": "",
    "email": "",
    "linkedin": "",
    "github": "",
    "website": ""
  },
  "summary": "",
  "work_experience": [
    {
      "job_title": "",
      "company": "",
      "location": {
        "city": "",
        "state": ""
      },
      "start_date": "",
      "end_date": "",
      "description": "",
      "achievements": [""]
    }
  ],
  "education": [
    {
      "degree": "",
      "field_of_study": "",
      "institution": "",
      "location": {
        "city": "",
        "state": ""
      },
      "start_date": "",
      "end_date": "",
      "honors": [""]
    }
  ],
  "skills": [""],
  "certifications": [
    {
      "title": "",
      "issuer": "",
      "date_obtained": "",
      "expiration_date": ""
    }
  ],
  "projects": [
    {
      "title": "",
      "description": "",
      "technologies": [""],
      "url": ""
    }
  ],
  "languages": [
    {
      "language": "",
      "proficiency": ""
    }
  ],
  "volunteer_experience": [
    {
      "role": "",
      "organization": "",
      "location": {
        "city": "",
        "state": ""
      },
      "start_date": "",
      "end_date": "",
      "description": ""
    }
  ],
  "interests": [""],
  "references": [
    {
      "name": "",
      "relationship": "",
      "contact_info": {
        "phone": "",
        "email": ""
      }
    }
  ]
}
"""

LLM_PROMPT = """
You are an expert at reading and understanding resumes.
Given the content of a CV or resume (provided below), extract all possible information and organize it into the following structured JSON schema.

Use arrays/lists as defined.
Preserve all sections, even if empty arrays.
For addresses and dates, fill in as much information as is available; leave missing fields as empty strings or null.
Return only valid JSON—no explanations or extra text.

json_schema = ```json 
{resume_schema}
```

CV text:
{resume_text}

Instructions:
Parse the above CV and output the structured data strictly according to the schema.
Leave values blank or use empty strings/arrays if data is missing from the CV.

Ensure the JSON is valid and well-formed.
"""