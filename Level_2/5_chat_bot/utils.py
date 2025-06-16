import json

import requests


def call_llama(model, prompt, stream=False):
    url = 'http://localhost:11434/api/generate'
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "stream": stream,
        "prompt": prompt,
    }
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to get response from LLaMA API. Error: {response.status_code}"