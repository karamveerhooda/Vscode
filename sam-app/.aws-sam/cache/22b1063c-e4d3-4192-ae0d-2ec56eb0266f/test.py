from os import rename, write
import json
import boto3
import requests
import yaml
from yaml.loader import SafeLoader 
from botocore.session import Session
from botocore.config import Config

def lambda_handler(event, context):
    # Set the source and destination file names
    source_bucket = 'filetransferpocr'
    source_file = 'File-A.txt'
    destination_bucket = 'filetransferpocr'
    destination_file = 'File-B.txt'
    
    
 # Create an S3 client 
    s3 = boto3.client('s3')
    try:
        print("inside try")
        # Retrieve the content of the YAML file
        raw_content_url = 'https://raw.githubusercontent.com/abdulkhadar-Capgemini/Process/fb84461be8d86e232f39f6436cdeec97750b04a5/process.yaml'
        # Make an HTTP GET request to the raw content URL
        response = requests.get(raw_content_url)
        response.raise_for_status()  # Raise an exception if the request is unsuccessful
        # Parse the YAML content
        yaml_content = yaml.safe_load(response.text)
        key1_value = yaml_content['Payload']['key1'].strip()
            
        # Compare the filename with the S3 bucket contents
        matching_files = [obj['Key'] for obj in response['Contents'] if obj['Key'] == key1_value]
        if matching_files:
          print(f"File '{key1_value}' found in S3 bucket.")
          file_merge(source_bucket,destination_bucket,source_file,destination_file)   
        else:
            return {
            'statusCode': 500,
            'body': f"File '{key1_value}' not found in S3 bucket."}
            

        def file_merge(source_bucket,destination_bucket,source_file,destination_file):
                response = s3.get_object(Bucket=source_bucket, Key=source_file)
                source_content = response['Body'].read().decode('utf-8')

                response = s3.get_object(Bucket=destination_bucket, Key=destination_file)
                destination_content = response['Body'].read().decode('utf-8')
                merged_content = destination_content + "\n" + source_content

                s3.put_object(Bucket=destination_bucket, Key=destination_file, Body=merged_content, ACL='private')

  #      return yaml_content_original
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }