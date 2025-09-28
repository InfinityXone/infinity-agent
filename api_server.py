#!/usr/bin/env python3
from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

AGENT_API_KEY = os.getenv("AGENT_ONE_API_KEY", "missing-key")

@app.route("/handshake", methods=["POST"])
def handshake():
    data = request.json
    if not data or "signature" not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    if data["signature"] != AGENT_API_KEY:
        return jsonify({"status": "error", "message": "Invalid signature"}), 403

    return jsonify({
        "status": "ok",
        "agent_id": data.get("agent_id"),
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Handshake successful"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running", "timestamp": datetime.utcnow().isoformat()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
