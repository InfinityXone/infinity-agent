#!/bin/bash

echo "🔁 Infinity Agent Parallel Monitor Started"
LOG_FILE="/mnt/data/infinity-agent/logs/parallel_health.log"
SCRIPTS_DIR="/mnt/data/infinity-agent/scripts"

# Ensure log path exists
mkdir -p $(dirname "$LOG_FILE")
touch "$LOG_FILE"

while true; do
  echo "🧠 [$(date)] Running GPT Sync Test" >> "$LOG_FILE"
  source /mnt/data/infinity-agent/venv/bin/activate && python "$SCRIPTS_DIR/gpt_sync_test.py" >> "$LOG_FILE" 2>&1

  echo "💾 [$(date)] Checking Supabase Memory Table" >> "$LOG_FILE"
  python "$SCRIPTS_DIR/memory_integrity_check.py" >> "$LOG_FILE" 2>&1

  echo "🖥️ [$(date)] Capturing System Health Snapshot" >> "$LOG_FILE"
  bash "$SCRIPTS_DIR/system_health_check.sh" >> "$LOG_FILE" 2>&1

  echo "📅 [$(date)] Checking Cron Status" >> "$LOG_FILE"
  bash "$SCRIPTS_DIR/cron_status_check.sh" >> "$LOG_FILE" 2>&1

  echo "✅ [$(date)] All checks complete. Sleeping for 10 minutes..." >> "$LOG_FILE"
  echo "----------------------------------------------------------" >> "$LOG_FILE"

  sleep 600
done
