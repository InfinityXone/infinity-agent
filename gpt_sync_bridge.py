import os
import time
import shutil
import subprocess

SOURCE_DIR = "/mnt/data/gpt_sync_payload"
TARGET_DIR = "/mnt/data/infinity-agent"
PROMPT_DIR = os.path.join(TARGET_DIR, "prompts")
AGENTS_DIR = os.path.join(TARGET_DIR, "agents")
UTILS_DIR = os.path.join(TARGET_DIR, "utils")
MEMORY_DIR = os.path.join(TARGET_DIR, "memory")
LOG_FILE = os.path.join(TARGET_DIR, "logs/sync_bridge.log")

os.makedirs(SOURCE_DIR, exist_ok=True)
os.makedirs(PROMPT_DIR, exist_ok=True)
os.makedirs(AGENTS_DIR, exist_ok=True)
os.makedirs(UTILS_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {msg}\n")

def move_file_smart(src_path, filename):
    extension = filename.split('.')[-1].lower()
    dst_path = None

    # Memory & ingestion trigger
    if extension in ["sql", "json", "txt", "log", "md"]:
        dst_path = os.path.join(MEMORY_DIR, filename)
        shutil.move(src_path, dst_path)
        log(f"🧠 Moved memory file: {filename}")
        try:
            subprocess.run(["python3", "agents/rosetta_ingest_patch.py"], cwd=TARGET_DIR)
            log(f"✅ Triggered memory ingestion: {filename}")
        except Exception as e:
            log(f"❌ Ingestion failed: {e}")
        return

    # Agent logic
    elif extension == "py":
        if "agent" in filename:
            dst_path = os.path.join(AGENTS_DIR, filename)
        elif "util" in filename or "helper" in filename:
            dst_path = os.path.join(UTILS_DIR, filename)
        else:
            dst_path = os.path.join(TARGET_DIR, filename)

    # Prompt logic
    elif extension == "md":
        dst_path = os.path.join(PROMPT_DIR, filename)

    else:
        dst_path = os.path.join(TARGET_DIR, filename)

    shutil.move(src_path, dst_path)
    log(f"✅ Moved {filename} → {dst_path}")

    # Local Git log only
    try:
        subprocess.run(["git", "add", "."], cwd=TARGET_DIR)
        subprocess.run(["git", "commit", "-m", f"🔄 Auto-sync: {filename}"], cwd=TARGET_DIR)
        log(f"📦 Git committed {filename}")
    except Exception as e:
        log(f"⚠️ Git commit failed: {e}")

print("🤖 GPT Sync Bridge running...")
log("🟢 Bridge started.")

while True:
    files = os.listdir(SOURCE_DIR)
    for file in files:
        src = os.path.join(SOURCE_DIR, file)
        if os.path.isfile(src):
            move_file_smart(src, file)
    time.sleep(10)
