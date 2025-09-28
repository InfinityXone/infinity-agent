
import json
import uuid
from codex import run_trance
import os

def dispatch_swarm(specs):
    swarm_id = str(uuid.uuid4())
    results = []
    for i, spec in enumerate(specs):
        output = run_trance(spec)
        out_path = f"/mnt/data/infinity-agent/output/{swarm_id}/agent_{i}.txt"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            f.write(output)
        results.append({"id": f"agent_{i}", "output_path": out_path})
    return {"swarm_id": swarm_id, "agents": results}
