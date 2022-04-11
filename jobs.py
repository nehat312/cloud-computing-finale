import pandas as pd
import boto3
from config import *


url = 'https://raw.githubusercontent.com/alexiskaldany/cloud-computing-finale/main/Suhas%20/Dataset.csv'
df =  pd.read_csv(url)
s3_bucket = 'cloud-computing-project-akaldany'
region = 'us-east-1'
key_name = 'test.csv'
s3_URI = f"https://{s3_bucket}.s3.{region}.amazonaws.com/{key_name}"
df.to_csv(s3_URI,storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key})