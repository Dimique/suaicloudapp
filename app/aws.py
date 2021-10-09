import requests
import boto3
from botocore.client import ClientError
from app import config

def check_s3_access():
    bucket_name = config.cfg['s3']['bucket']
    if len(bucket_name) == 0:
        return False
    
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False
        # The bucket does not exist or you have no access.

def get_instance_hostname():
    url = 'http://169.254.169.254/latest/meta-data/hostname'
    hostname = requests.get(url).text
    return hostname
