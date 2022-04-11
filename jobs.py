#%%
import pandas as pd
import boto3
from config import *


url = 'https://raw.githubusercontent.com/alexiskaldany/cloud-computing-finale/main/Suhas%20/Dataset.csv'
df =  pd.read_csv(url)
s3_bucket = 'cloud-computing-project-akaldany/'
region = 'us-east-1'
key_name = 'prediction.csv'
s3_URI = f"s3://{s3_bucket}{key_name}"
#%%
df.to_csv(s3_URI,storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key})
# %%
