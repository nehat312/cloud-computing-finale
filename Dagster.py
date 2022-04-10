## File for Dagster Operations
from dagster import job, op
import pandas as pd
import boto3 
    
# Variables
"""
url = 'https://www.kaggle.com/datasets/pablote/nba-enhanced-stats?select=2012-18_teamBoxScore.csv'
"""    
    
@op
def scrape_data(url: str):
    """scrape operation

    Args:
        url (str): url to be turned into dataframe
    """
    df =  pd.read_csv(url)    
    return df

@op
def to_s3(object):
    
    