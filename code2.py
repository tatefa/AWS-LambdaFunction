import json
import boto3
import base64
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket name and file details from the event
    bucket_name = os.environ['BUCKET_NAME']
    file_name = event['file_name']
    file_content = event['file_content']  # Base64 encoded content
    
    # Decode the base64 content
    file_data = base64.b64decode(file_content)
    
    # Upload the file to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'File {file_name} uploaded successfully to {bucket_name}.'
        })
    }
