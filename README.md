# Infinity Agent: Codex Prime

Infinity Agent is a headless, API-driven orchestration framework designed for full GPT integration, cloud deployment, agent self-replication, and prompt mutation at scale.

## Core Components
- `gateway.py` – Secure API Gateway for agent access
- `ipc_server.py` – Local socket server for internal coordination
- `ipc_client.py` – CLI client to send local instructions
- `gpt_sync_bridge.py` – Bidirectional GPT ↔ Agent communication via API

## Quick Start
```bash
bash install_infinity_agent.sh
```

## GPT Integration
Configure `.env` with your GPT or Groq keys, set sync endpoints, and you're live.

