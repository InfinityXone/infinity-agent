
from fastapi import FastAPI, Request, HTTPException
from codex import run_trance
import os
import uuid
from dotenv import load_dotenv
from starlette.middleware.base import BaseHTTPMiddleware
from ipaddress import ip_address, ip_network
import json
import socket

load_dotenv()

AGENT_API_KEY = os.getenv("AGENT_ONE_API_KEY")
ENABLE_AUTH = os.getenv("ENABLE_AUTH", "true").lower() == "true"
AGENT_NAME = os.getenv("AGENT_NAME", "Unnamed Agent")
AGENT_ROLE = os.getenv("AGENT_ROLE", "Unknown")
P_WHITELIST = os.getenv("P_WHITELIST", "127.0.0.1").split(",")
IPC_SOCKET_PATH = os.getenv("IPC_SOCKET_PATH", "/tmp/agent_one.sock")

app = FastAPI()

def ip_allowed(client_ip):
    for net in P_WHITELIST:
        try:
            if ip_address(client_ip) in ip_network(net):
                return True
        except:
            continue
    return False

@app.middleware("http")
async def secure_gate(request: Request, call_next):
    client_ip = request.client.host
    if not ip_allowed(client_ip):
        raise HTTPException(status_code=403, detail="IP not allowed")

    if ENABLE_AUTH:
        if request.headers.get("X-Agent-Key") != AGENT_API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key")
    return await call_next(request)

@app.get("/handshake")
async def handshake():
    return {
        "agent": AGENT_NAME,
        "role": AGENT_ROLE,
        "status": "live",
        "secure": ENABLE_AUTH,
        "ip_whitelist": P_WHITELIST,
        "ipc": IPC_SOCKET_PATH
    }

@app.post("/build")
async def build(request: Request):
    body = await request.json()
    spec = body.get("spec", "")
    feedback = body.get("feedback", None)
    output, snapshot_id = run_trance(spec) if not feedback else run_trance(spec, feedback)
    return {
        "status": "success",
        "snapshot_id": snapshot_id,
        "agent": AGENT_NAME,
        "spec": spec
    }

@app.get("/swarm/status")
def swarm_status():
    reg_file = os.path.join(os.path.dirname(__file__), "swarm_registry.json")
    if not os.path.exists(reg_file):
        return {"swarm": []}
    with open(reg_file) as f:
        return json.load(f)
