from constants import *
import boto3
import os

client = boto3.client('s3',
                      aws_access_key_id="YOUR_ACCESS_KEY_ID",
                      aws_secret_access_key="YOUR_ACCESS_KEY"
                      )

root_path = os.getcwd()
print(f"root_path : {root_path}")
file_name = "receipt.txt"

file_path = os.path.join(root_path, file_name)
print(f"file_path : {file_path}")

bucket_name = "mohammadbucket"


client.upload_file(file_path, bucket_name, file_name)
