import boto3
from botocore.exceptions import ClientError
import os

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

def upload_to_s3(bucket: str, key: str, content: str) -> str:
    s3 = get_s3_client()
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
        return key
    except ClientError as e:
        raise Exception(f"Failed to upload to S3: {e}")


def create_s3_folders(bucket: str, folders: list[str]) -> None:
    s3 = get_s3_client()
    for folder in folders:
        if not folder.endswith("/"):
            folder += "/"
        s3.put_object(Bucket=bucket, Key=folder)

