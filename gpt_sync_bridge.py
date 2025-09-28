import os
import time
import shutil
import subprocess

SOURCE_DIR = "/mnt/data/gpt_sync_payload"
TARGET_DIR = "/mnt/data/infinity-agent"
PROMPT_DIR = os.path.join(TARGET_DIR, "prompts")
AGENTS_DIR = os.path.join(TARGET_DIR, "agents")
UTILS_DIR = os.path.join(TARGET_DIR, "utils")
LOG_FILE = os.path.join(TARGET_DIR, "logs/sync_bridge.log")

os.makedirs(SOURCE_DIR, exist_ok=True)
os.makedirs(PROMPT_DIR, exist_ok=True)
os.makedirs(AGENTS_DIR, exist_ok=True)
os.makedirs(UTILS_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {msg}\n")

def move_file_smart(src_path, filename):
    extension = filename.split('.')[-1]
    dst_path = None

    if extension == "py":
        if "agent" in filename:
            dst_path = os.path.join(AGENTS_DIR, filename)
        elif "util" in filename or "helper" in filename:
            dst_path = os.path.join(UTILS_DIR, filename)
        else:
            dst_path = os.path.join(TARGET_DIR, filename)

    elif extension == "md":
        dst_path = os.path.join(PROMPT_DIR, filename)

    elif extension in ["sql", "json", "txt"]:
        dst_path = os.path.join(TARGET_DIR, "data_ingest", filename)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        try:
            subprocess.run(["python3", "scripts/rosetta_ingest.py", dst_path], cwd=TARGET_DIR)
            log(f"🧠 Triggered memory ingestion for {filename}")
        except Exception as e:
            log(f"⚠️ Failed to ingest {filename}: {e}")

    else:
        dst_path = os.path.join(TARGET_DIR, filename)

    shutil.move(src_path, dst_path)
    log(f"✅ Moved {filename} → {dst_path}")

def git_log_change(filename):
    try:
        subprocess.run(["git", "add", "."], cwd=TARGET_DIR)
        subprocess.run(["git", "commit", "-m", f"🔄 Auto-integrated: {filename}"], cwd=TARGET_DIR)
        log(f"📦 Git committed {filename}")
    except Exception as e:
        log(f"⚠️ Git commit failed: {e}")

print("🤖 Smart GPT Sync Bridge Running...")
log("🟢 Sync bridge booted.")

while True:
    files = os.listdir(SOURCE_DIR)
    for file in files:
        src = os.path.join(SOURCE_DIR, file)
        if os.path.isfile(src):
            move_file_smart(src, file)
            git_log_change(file)

    time.sleep(10)
