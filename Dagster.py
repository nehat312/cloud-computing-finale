## File for Dagster Operations
from dagster import job, op, get_dagster_logger
import pandas as pd
import boto3 
    
# Variables
"""
url = 'https://www.kaggle.com/datasets/pablote/nba-enhanced-stats?select=2012-18_teamBoxScore.csv'
"""    
    
@op
def scrape_data(url: str):
    """scrape operation, point at online csv links

    Args:
        url (str): url to be turned into dataframe
    """
    df =  pd.read_csv(url)
    if isinstance(df,pd.DataFrame) == True:
        get_dagster_logger().info(f"Url {url} succesfully converted to Dataframe")
    else:
        get_dagster_logger().info(f"Url {url} failed to be converted to Dataframe")
    return df

@op
def df_from_s3(s3_bucket,region,key_name):
    """saves object to s3 bucket

    Args:
        df (pd.Dataframe): a pandas dataframe
        s3_bucket (str): bucket within s3
        region (str): AWS region (like us-east-1)
        key_name: name of object within bucket (could be within a subfolder like /data/example.csv)
        
        example: https://bucket-name.s3.Region.amazonaws.com/key-name
        s3_bucket = bucket-name
        
    """
    s3_URI = f"https://{s3_bucket}.s3.{region}.amazonaws.com/{key_name}"
    try:
        df = pd.DataFrame(s3_URI)
        get_dagster_logger().info(f"Dataframe: {df} succesfully loaded from s3 {s3_bucket} at path {key_name}")
    except:
        get_dagster_logger().info(f"Dataframe: {df} failed to load from s3 {s3_bucket} at path {key_name}")


@op
def df_to_s3(df,s3_bucket,region,key_name):
        """saves object to s3 bucket

        Args:
        df (pd.Dataframe): a pandas dataframe
        s3_bucket (str): bucket within s3
        region (str): AWS region (like us-east-1)
        key_name: name of object within bucket (could be within a subfolder like /data/example.csv)

        example: https://bucket-name.s3.Region.amazonaws.com/key-name
        s3_bucket = bucket-name

        """
        s3_URI = f"https://{s3_bucket}.s3.{region}.amazonaws.com/{key_name}"
        try:
            df.to_csv(s3_URI)
            get_dagster_logger().info(f"Dataframe: {df} succesfully saved to s3 {s3_bucket} at path {key_name}")
            return 
        except:
            get_dagster_logger().info(f"Dataframe: {df} failed to save to s3 {s3_bucket} at path {key_name}")
 
@op           
def df_pre_processing(df):
    cols = ['gmDate', 'gmTime', 'seasTyp', 'teamAbbr','teamPTS', 'teamAST', 'teamTO', 'teamSTL', 'teamBLK', 'teamPF', 'teamFG%', 'team3P%', 'teamFT%', 'teamTRB','teamRslt', 'teamOrtg', 'teamDrtg',  'opptAbbr', 'opptPTS', 'opptAST', 'opptTO', 'opptSTL', 'opptBLK', 'opptPF', 'opptFG%', 'oppt3P%', 'opptFT%', 'opptTRB', 'opptOrtg', 'opptDrtg']
    df_filtered = df[cols].copy()