# supabase_connection_test.py
# Tests Supabase connection and writes to system_logs

from dotenv import load_dotenv
import os
from supabase import create_client
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path="/mnt/data/infinity-agent/.env")

# Retrieve Supabase credentials
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_SERVICE_KEY in environment variables!")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# Test payload
test_entry = {
    "source": "CONNECTION_TEST",
    "level": "INFO",
    "message": "Supabase connection verified successfully",
    "data": {
        "timestamp": datetime.utcnow().isoformat(),
        "status": "success",
        "test_run": True
    }
}

# Insert log into system_logs
print("🔗 Connecting to Supabase and writing test log...")
response = supabase.table("system_logs").insert(test_entry).execute()

# Output
if response.data:
    print("✅ Test successful! Log entry created:")
    print(response.data)
else:
    print("❌ Test failed!")
    print(response)
