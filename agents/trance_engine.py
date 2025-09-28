
import os
import uuid
from codex import call_groq
from datetime import datetime

SNAPSHOT_DIR = "/mnt/data/infinity-agent/snapshots"

def save_snapshot(prompt, response):
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    snapshot_id = f"{datetime.now().isoformat()}_{uuid.uuid4()}"
    with open(f"{SNAPSHOT_DIR}/{snapshot_id}.md", "w") as f:
        f.write(f"# Prompt\n{prompt}\n\n# Response\n{response}")
    return snapshot_id

def mutate_prompt(base_prompt, feedback):
    return f"{base_prompt}\n\n# Mutation based on feedback:\n{feedback}"

def run_codex_trance(spec, feedback=None):
    base_prompt = f"""You are Codex Prime. Build and deploy based on this spec:

--- SPEC ---
{spec}
--- END SPEC ---

Phases: Plan → Code → Push → Deploy → Log → Expose.
"""
    if feedback:
        base_prompt = mutate_prompt(base_prompt, feedback)

    response = call_groq(base_prompt)
    snapshot_id = save_snapshot(base_prompt, response)
    return response, snapshot_id
