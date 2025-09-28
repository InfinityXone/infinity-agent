
from fastapi import FastAPI, Request
from codex import run_trance
import os
import uuid

app = FastAPI()

@app.post("/build")
async def build(request: Request):
    body = await request.json()
    spec = body.get("spec", "")
    project_id = str(uuid.uuid4())
    output = run_trance(spec)

    path = f"/mnt/data/infinity-agent/output/{project_id}.txt"
    with open(path, "w") as f:
        f.write(output)

    return {
        "status": "complete",
        "project_id": project_id,
        "output_path": path
    }
