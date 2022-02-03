import boto3, botocore
from flask import current_app as app

s3 = boto3.client(
    "s3",
    aws_access_key_id = app.config["AWS_ACCESS_KEY"],
    aws_secret_access_key = app.config["AWS_SECRET_ACCESS_KEY"]
)