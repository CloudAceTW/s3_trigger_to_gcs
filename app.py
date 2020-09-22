import os
import boto3
import uuid

from chalice import Chalice
from google.cloud import storage


app = Chalice(app_name="s3_trigger_to_gcs")


@app.on_s3_event(bucket=os.getenv("s3_bucket"), events=["s3:ObjectCreated:*"])
def handler(event):
    bucket = event.bucket
    key = event.key

    s3 = boto3.client("s3")

    file_path = f"/tmp/{uuid.uuid4()}{key.replace('/', '')}"

    s3.download_file(bucket, key, file_path)

    client = storage.Client.from_service_account_json(
        "/var/task/chalicelib/gcs_credential/service_account.json"
    )
    bucket = client.get_bucket(os.getenv("gcs_bucket"))
    bucket.blob(event.key).upload_from_filename(file_path)
