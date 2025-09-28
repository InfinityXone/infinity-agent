import requests
import os

webhook_url = os.getenv("VERCEL_WEBHOOK_URL")
res = requests.post(webhook_url)
print("Vercel Trigger:", res.status_code, res.text)
