import os
from google.cloud import storage

client = storage.Client.from_service_account_json(os.getenv("GCP_SERVICE_ACCOUNT_JSON"))
bucket = client.get_bucket(os.getenv("GCP_BUCKET_NAME"))
path = "/mnt/data/infinity-agent/output"

for filename in os.listdir(path):
    local_path = os.path.join(path, filename)
    blob = bucket.blob(f"infinity-agent/{filename}")
    blob.upload_from_filename(local_path)
    print(f"Uploaded: {filename}")
