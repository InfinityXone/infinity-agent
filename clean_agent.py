
import os
import time
import shutil
from datetime import datetime, timedelta

base_path = "/mnt/data/infinity-agent"

def clean_old_files(folder, days=2):
    now = time.time()
    cutoff = now - (days * 86400)
    for root, dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            if os.path.getmtime(path) < cutoff:
                os.remove(path)

def compress_output():
    output_dir = os.path.join(base_path, "output")
    archive_dir = os.path.join(base_path, "output", "archives")
    os.makedirs(archive_dir, exist_ok=True)
    for f in os.listdir(output_dir):
        path = os.path.join(output_dir, f)
        if os.path.isfile(path) and f.endswith(".txt"):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            shutil.copy(path, f"{archive_dir}/{timestamp}_{f}")

def clean():
    clean_old_files(os.path.join(base_path, "logs"))
    clean_old_files(os.path.join(base_path, "snapshots"))
    compress_output()

if __name__ == "__main__":
    clean()
