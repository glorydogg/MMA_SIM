import boto3
import os
from dotenv import load_dotenv

class S3Uploader:
    def __init__(self):
        # load env variables from .env
        load_dotenv()

        # Retrieve AWS creditionals and config
        self.bucket = os.getenv ("AWS_BUCKET_NAME")
        self.region = os.getenv("AWS_REGION")

        self.aws_access_key = os.getenv("AWS_ACCESS-KEY")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        # Initialize client
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region
        )

    def upload(self, local_path, s3_key):
        """ Uploads a file to s3 bucket """
        try:
            self.s3.upload_file(local_path, self.bucket, s3_key)
            print(f"[AWS] Uploaded {local_path} -> s3://{self.bucket}/{s3_key}")
        except Exception as e:
            print(f"[AWS ERROR] {e}")