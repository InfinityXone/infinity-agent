
from utils.env_loader import load_environment
import requests
import openai

env = load_environment()

def call_groq(prompt):
    headers = {
        "Authorization": f"Bearer {env['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": env["MODEL_GROQ"],
        "messages": [{"role": "system", "content": prompt}]
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("GROQ failed, falling back to OpenAI:", e)
        return call_openai(prompt)

def call_openai(prompt):
    openai.api_key = env["OPENAI_API_KEY"]
    try:
        response = openai.ChatCompletion.create(
            model=env["MODEL_OPENAI"],
            messages=[{"role": "system", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI Fallback Error: {str(e)}"

def run_trance(spec_text):
    trance_prompt = f"""
You are Codex Prime. Execute the following build:

--- SPEC START ---
{spec_text}
--- SPEC END ---

Phases: plan → code → push → deploy → log → expose.
"""
    return call_groq(trance_prompt)
