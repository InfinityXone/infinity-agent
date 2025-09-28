
import os
from dotenv import load_dotenv

def load_environment():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path=env_path)

    return {
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "MODEL_GROQ": os.getenv("MODEL_GROQ", "mixtral-8x7b-32768"),
        "MODEL_OPENAI": os.getenv("MODEL_OPENAI", "gpt-4o"),
        "SUPABASE_URL": os.getenv("SUPABASE_URL"),
        "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
        "GCP_KEY_PATH": os.getenv("GCP_KEY_PATH"),
        "VERCEL_TOKEN": os.getenv("VERCEL_TOKEN"),
        "GIT_REMOTE": os.getenv("GIT_REMOTE"),
        "AGENT_ONE_API_KEY": os.getenv("AGENT_ONE_API_KEY")
    }
