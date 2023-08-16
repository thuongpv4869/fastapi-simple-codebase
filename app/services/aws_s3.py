import boto3

from app.config import settings

s3 = boto3.resource("s3")

bucket = s3.Bucket(settings.AWS_S3_DEFAULT_BUCKET)
