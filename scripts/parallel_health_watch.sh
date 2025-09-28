#!/bin/bash

LOG_FILE="/mnt/data/infinity-agent/logs/parallel_health.log"
SCRIPTS_DIR="/mnt/data/infinity-agent/scripts"

mkdir -p $(dirname "$LOG_FILE")
touch "$LOG_FILE"

while true; do
  echo "-----------------------------" >> "$LOG_FILE"
  echo "🧠 [$(date)] GPT Sync Check" >> "$LOG_FILE"
  python3 "$SCRIPTS_DIR/gpt_sync_test.py" >> "$LOG_FILE" 2>&1

  echo "💾 [$(date)] Supabase Memory Check" >> "$LOG_FILE"
  python3 "$SCRIPTS_DIR/memory_integrity_check.py" >> "$LOG_FILE" 2>&1

  echo "🖥️ [$(date)] System Check" >> "$LOG_FILE"
  bash "$SCRIPTS_DIR/system_health_check.sh" >> "$LOG_FILE" 2>&1

  echo "📅 [$(date)] Cron Check" >> "$LOG_FILE"
  bash "$SCRIPTS_DIR/cron_status_check.sh" >> "$LOG_FILE" 2>&1

  echo "✅ Health snapshot complete." >> "$LOG_FILE"
  sleep 600
done
