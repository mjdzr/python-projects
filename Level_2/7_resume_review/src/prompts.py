RESUME_JSON_SCHEMA = """
{
  "personal_info": {
    "full_name": "",
    "address": {
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

LLM_JSON_PARSE_PROMPT = """
You are an expert at reading and understanding resumes.
Given the content of a CV or resume (provided below), extract all possible information and organize it into the following structured JSON schema.

Use arrays/lists as defined.
Preserve all sections, even if empty arrays.
For addresses and dates, fill in as much information as is available; leave missing fields as empty strings or null.
Return only valid JSON—no explanations or extra text.

**json_schema** = ```json 
{resume_schema}
```

CV text:
{resume_text}

Instructions:
Parse the above CV and output the structured data strictly according to the schema.
Leave values blank or use empty strings/arrays if data is missing from the CV.

Note: Ensure the JSON is valid and well-formed.
"""

RESUME_YAML_SCHEMA = """
  personal_info:
    full_name: string
    address:
      street: string
      city: string
      state: string
      zip: string
      country: string
    phone: string
    email: string
    linkedin: string
    github: string
    website: string
  summary: string
  work_experience:
    - job_title: string
      company: string
      location:
        city: string
        state: string
      start_date: date
      end_date: date
      description: string
      achievements:
        - string
  education:
    - degree: string
      field_of_study: string
      institution: string
      location:
        city: string
        state: string
      start_date: date
      end_date: date
      honors:
        - string
  skills:
    - string
  certifications:
    - title: string
      issuer: string
      date_obtained: date
      expiration_date: date
  projects:
    - title: string
      description: string
      technologies:
        - string
      url: string
  languages:
    - language: string
      proficiency: string
  volunteer_experience:
    - role: string
      organization: string
      location:
        city: string
        state: string
      start_date: date
      end_date: date
      description: string
  interests:
    - string
  references:
    - name: string
      relationship: string
      contact_info:
        phone: string
        email: string
"""

LLM_YAML_PARSE_PROMPT = """
You are an expert at reading and understanding resumes.
Given the content of a CV or resume (provided below), extract all possible information and organize it into the following structured YAML schema.
Use arrays/lists as defined.
Preserve all sections, even if empty arrays.

For addresses and dates, fill in as much information as is available; leave missing fields as empty strings or null.
Return only valid YAML—no explanations or extra text.
**yaml_schema** = ```yaml
{resume_schema}
```
CV text:
{resume_text}
Instructions:
Parse the above CV and output the structured data strictly according to the schema.
Leave values blank or use empty strings/arrays if data is missing from the CV.

Note: Ensure the YAML is valid and well-formed.
"""

REVIEW_OUTPUT_SCHEMA = """
section_name_1:
  impact_level: string
  revised_content: string | list | dict
  revision_suggestion: list[string]
section_name_2:
  impact_level: string
  revised_content: string | list | dict
  revision_suggestion: list[string]
...
"""

RESUME_REVIEW_PROMPT = """
**Task:** You are an expert resume reviewer. Your job is to analyze the provided resume data in YAML format and suggest improvements for each section. For each suggestion, you should provide an impact score (Low, Medium, High) and the revised version.

**YAML Input Data:** {resume_data}

**Instructions:**

1. Read the provided YAML resume data carefully.
2. For each section, evaluate the content and suggest improvements.
3. For each suggestion, include:
   - An impact score (Low, Medium, High).
   - The revised version of the text.
   - Suggestion on how to improve the section.

**YAML Output Schema:**

```yaml
{review_output_schema}
```

**Output Requirement:**

- Please provide the output strictly in the above YAML format, without any additional explanations or text.
- Make sure to add double quotes around the values that are strings. This is important for the YAML parser.
"""