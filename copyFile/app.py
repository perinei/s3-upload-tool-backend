import boto3
import os
from urllib.parse import unquote

s3 = boto3.resource('s3',verify=True,region_name=os.environ['AWS_REGION'])

def lambda_handler(event, context):
    print('copy file started')
    print(event)
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        source_key_durty = record['s3']['object']['key']
        source_key = unquote(source_key_durty)
    print("source bucket")
    print(source_bucket)
    print("source key")
    print(source_key)
    email = source_key.split('/')[2]
    file_name = source_key.split('/')[3]
    print("relailer name")
    print(email)
    print("file name")
    print(file_name)
    copy_source = {
    'Bucket': source_bucket,
    'Key': source_key
    }
    bucket = s3.Bucket(source_bucket)
    bucket.copy(copy_source, "processedFiles" + "/" + email + "-" + file_name)
    print("copy file complete")





