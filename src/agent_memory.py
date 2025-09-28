from supabase import create_client
import os, json

supabase = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_SERVICE_KEY'])

def log_task(task_id, status, input_data=None, output_data=None, metadata=None):
    supabase.table("agent_memory").insert({
        "task_id": task_id,
        "status": status,  # pending, running, completed, failed
        "input_data": json.dumps(input_data) if input_data else None,
        "output_data": json.dumps(output_data) if output_data else None,
        "metadata": json.dumps(metadata) if metadata else None
    }).execute()
