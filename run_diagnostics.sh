#!/bin/bash

echo "🔍 Running Infinity Agent Diagnostics..."

# 1. Check if main agent directory exists
if [ -d "/mnt/data/infinity-agent" ]; then
  echo "✅ /mnt/data/infinity-agent exists."
else
  echo "❌ /mnt/data/infinity-agent is missing!"
fi

# 2. Check if ports 8000 and 8001 are open (neural handshake)
check_port() {
  PORT=$1
  if nc -zv localhost $PORT 2>/dev/null; then
    echo "✅ Port $PORT is open (Agent handshake confirmed)"
  else
    echo "⚠️ Port $PORT is not responding"
  fi
}

check_port 8000
check_port 8001

# 3. Check presence of key runtime scripts
echo "📦 Checking scripts/"
for file in git_push.sh supabase_sync.py gcs_uploader.py vercel_trigger.py rosetta_ingest.py; do
  if [ -f "/mnt/data/infinity-agent/scripts/$file" ]; then
    echo "✅ Found: $file"
  else
    echo "❌ Missing: $file"
  fi
done

# 4. Logs check
[ -d "/mnt/data/infinity-agent/logs" ] || mkdir -p /mnt/data/infinity-agent/logs

# 5. GPT Sync Bridge check
[ -f "/mnt/data/infinity-agent/gpt_sync_bridge.py" ] && echo "🧠 GPT Sync Bridge is present." || echo "❌ GPT Sync Bridge missing."

echo "✅ Diagnostics complete."
