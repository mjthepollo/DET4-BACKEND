import logging
import os

import boto3
import openai

LOCAL = not (os.environ.get("LOCAL") == "False")
# LOCAL : app run by local and DEBUG True, in Labmda : use awsgi
if LOCAL:
    from dotenv import load_dotenv
    load_dotenv()
else:
    import awsgi

# Load the .env file


logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = os.environ.get("BUCKET_NAME")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


#AWS CLIENT INITIALIZE
if LOCAL:
    s3 = boto3.client('s3',
        region_name="ap-northeast-2",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )
    polly = boto3.client('polly',
        region_name="ap-northeast-2",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )
else:
    s3 = boto3.client('s3', region_name="ap-northeast-2")
    polly = boto3.client('polly', region_name="ap-northeast-2")

openai.api_key = OPENAI_API_KEY
polly_voice = "Seoyeon"