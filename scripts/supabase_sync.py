import os
import requests
import json

# Load .env values (mocked for simplicity)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
MEMORY_TABLE = os.getenv("AGENT_MEMORY_TABLE", "agent_memory")

data = {
    "agent_id": os.getenv("AGENT_ID"),
    "timestamp": str(__import__('datetime').datetime.utcnow()),
    "memory": "Current context memory sync..."
}

headers = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json"
}

res = requests.post(f"{SUPABASE_URL}/rest/v1/{MEMORY_TABLE}", json=data, headers=headers)
print("Supabase Sync:", res.status_code, res.text)
