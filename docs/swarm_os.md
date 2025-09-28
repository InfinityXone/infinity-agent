
# Swarm OS Protocol

Each agent runs a REST API with:
- /status
- /build
- /logs
- /ping

Agents announce themselves to a central hub with:
POST /handshake
{
    "agent_id": "...",
    "ip": "...",
    "status": "alive",
    "capabilities": ["build", "deploy", "scrape"]
}
