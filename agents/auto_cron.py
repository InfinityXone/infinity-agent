
import os

CRON_JOB_PATH = "/etc/cron.d/infinity-autopush"

def write_cron_job():
    job = "*/5 * * * * curl -X POST http://localhost:8080/build -H 'Content-Type: application/json' -d '{"spec": "Auto-cron scheduled build"}'\n"
    with open(CRON_JOB_PATH, "w") as f:
        f.write(job)
