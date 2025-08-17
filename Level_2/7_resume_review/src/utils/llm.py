import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from functools import cache

# Find and load the .env file
load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cache
def call_llm(prompt, model = "gpt-4.1"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that extracts information from resumes."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content