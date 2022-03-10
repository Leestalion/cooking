import boto3
from flask import current_app as app
import sys
from werkzeug.utils import secure_filename
import requests
from oauthlib.oauth2 import WebApplicationClient

s3 = boto3.client(
    "s3",
    aws_access_key_id = app.config["AWS_ACCESS_KEY"],
    aws_secret_access_key = app.config["AWS_SECRET_ACCESS_KEY"]
)


def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            app.config["AWS_BUCKET_NAME"],
            file.filename,
            ExtraArgs={
                "ACL":acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e :
        type, value, traceback = sys.exc_info()
        print("Exception Happened :", e)
        print("Error details : ", value)
        return e;
    
    return file.filename

def get_google_provider_cfg():
    return requests.get(app.config["GOOGLE_DISCOVERY_URL"]).json()


client = WebApplicationClient(app.config["GOOGLE_CLIENT_ID"])
