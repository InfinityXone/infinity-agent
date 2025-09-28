
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def send_to_gpt(prompt, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
