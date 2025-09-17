import os
from functools import cache

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

# Find and load the .env file
load_dotenv(find_dotenv())

assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY not found"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cache
def call_llm(prompt, model = "gpt-4.1-nano"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that translates information"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content