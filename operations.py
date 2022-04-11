## File for Dagster Operations
from dagster import op, job, get_dagster_logger
import pandas as pd

#logger = get_dagster_logger()
    
# Variables
# """
# url = 'https://raw.githubusercontent.com/alexiskaldany/cloud-computing-finale/main/Suhas%20/Dataset.csv'
# s3_bucket = 'cloud-computing-project-akaldany'
# region = 'us-east-1'
# key_name = 'test.csv'
# """    
#############  
@op
def scrape_data():
    """scrape operation, point at online csv links

    Args:
        url (str): url to be turned into dataframe
    """
    url = 'https://raw.githubusercontent.com/alexiskaldany/cloud-computing-finale/main/Suhas%20/Dataset.csv'
    df =  pd.read_csv(url)
    if isinstance(df,pd.DataFrame) == True:
        #logger().info(f"Url {url} succesfully converted to Dataframe")
        return df
    else:
        #logger().info(f"Url {url} failed to be converted to Dataframe")
        return df
##############
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
        #logger().info(f"Dataframe: {df} succesfully loaded from s3 {s3_bucket} at path {key_name}")
        return
    except:
       # logger().info(f"Dataframe: {df} failed to load from s3 {s3_bucket} at path {key_name}")
        return

@op
def df_to_s3(df):
        """saves object to s3 bucket

        Args:
        df (pd.Dataframe): a pandas dataframe
        s3_bucket (str): bucket within s3
        region (str): AWS region (like us-east-1)
        key_name: name of object within bucket (could be within a subfolder like /data/example.csv)

        example: https://bucket-name.s3.Region.amazonaws.com/key-name
        s3_bucket = bucket-name

        """
        s3_bucket = 'cloud-computing-project-akaldany'
        region = 'us-east-1'
        key_name = 'test.csv'
        s3_URI = f"https://{s3_bucket}.s3.{region}.amazonaws.com/{key_name}"
        try:
            df.to_csv(s3_URI)
            #logger().info(f"Dataframe: {df} succesfully saved to s3 {s3_bucket} at path {key_name}")
            return
        except:
            #logger().info(f"Dataframe: {df} failed to save to s3 {s3_bucket} at path {key_name}")
            return
@job
def scrape_csv_from_url():
    df_to_s3(scrape_data())
    #logger().info(f"URL has been scraped and saved")
    
    

    
# @op           
# def df_pre_processing(df):
#     cols = ['gmDate', 'gmTime', 'seasTyp', 'teamAbbr','teamPTS', 'teamAST', 'teamTO', 'teamSTL', 'teamBLK', 'teamPF', 'teamFG%', 'team3P%', 'teamFT%', 'teamTRB','teamRslt', 'teamOrtg', 'teamDrtg',  'opptAbbr', 'opptPTS', 'opptAST', 'opptTO', 'opptSTL', 'opptBLK', 'opptPF', 'opptFG%', 'oppt3P%', 'opptFT%', 'opptTRB', 'opptOrtg', 'opptDrtg']
#     df_filtered = df[cols].copy()
#     return df_filtered