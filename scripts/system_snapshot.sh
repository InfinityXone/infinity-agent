#!/bin/bash
# Infinity Agent - Full System Snapshot
# Collect logs, file tree, and package into a zip

SNAP_DIR="/mnt/data/infinity-agent/system_snapshot"
LOG_DIR="/mnt/data/infinity-agent/logs"
OUT_FILE="/mnt/data/system_snapshot_$(date +%Y%m%d_%H%M%S).zip"

mkdir -p "$SNAP_DIR"

echo "=== 🧠 Infinity Agent System Snapshot ===" > "$SNAP_DIR/summary.txt"
echo "[DATE] $(date)" >> "$SNAP_DIR/summary.txt"
echo "[HOST] $(hostname)" >> "$SNAP_DIR/summary.txt"
echo >> "$SNAP_DIR/summary.txt"

# 1. System Tree (3 levels deep)
echo "📂 Directory Tree (3 levels)" >> "$SNAP_DIR/summary.txt"
tree -L 3 /mnt/data/infinity-agent >> "$SNAP_DIR/summary.txt" 2>/dev/null
echo >> "$SNAP_DIR/summary.txt"

# 2. Active processes
echo "⚙️ Active Processes (Infinity Agent)" >> "$SNAP_DIR/summary.txt"
ps aux | grep infinity-agent | grep -v grep >> "$SNAP_DIR/summary.txt"
echo >> "$SNAP_DIR/summary.txt"

# 3. Cron jobs
echo "📅 Cron Jobs" >> "$SNAP_DIR/summary.txt"
crontab -l >> "$SNAP_DIR/summary.txt" 2>/dev/null
echo >> "$SNAP_DIR/summary.txt"

# 4. Systemd services (filter Infinity)
echo "🖥️ Systemd Services" >> "$SNAP_DIR/summary.txt"
systemctl list-units --type=service | grep infinity >> "$SNAP_DIR/summary.txt"
systemctl list-units --type=service | grep gpt_sync >> "$SNAP_DIR/summary.txt"
echo >> "$SNAP_DIR/summary.txt"

# 5. Logs (copy raw logs folder)
mkdir -p "$SNAP_DIR/logs"
cp -r "$LOG_DIR"/* "$SNAP_DIR/logs/" 2>/dev/null

# Package everything
cd /mnt/data
zip -r "$OUT_FILE" "$(basename $SNAP_DIR)" >/dev/null

echo "✅ Snapshot complete: $OUT_FILE"
