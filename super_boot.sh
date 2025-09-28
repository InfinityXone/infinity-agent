#!/bin/bash

echo "🚀 Launching Infinity Agent Supreme Runtime..."

cd /mnt/data/infinity-agent
source venv/bin/activate

# === Core Services ===
nohup venv/bin/python gateway.py > logs/gateway.log 2>&1 &
nohup venv/bin/python ipc_server.py > logs/ipc.log 2>&1 &

# === Git Cron ===
(crontab -l 2>/dev/null | grep -v git_push.sh; echo "*/2 * * * * /mnt/data/infinity-agent/scripts/git_push.sh") | crontab -

# === Memory + Cloud Sync Agents ===
nohup venv/bin/python scripts/supabase_sync.py > logs/supabase_sync.log 2>&1 &
nohup venv/bin/python scripts/gcs_uploader.py > logs/gcs_upload.log 2>&1 &
nohup venv/bin/python scripts/vercel_trigger.py > logs/vercel.log 2>&1 &
nohup venv/bin/python scripts/rosetta_ingest.py > logs/rosetta.log 2>&1 &

echo "✅ All agents running. Infinity Agent is now live."
