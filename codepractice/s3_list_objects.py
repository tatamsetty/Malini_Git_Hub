import boto3
#from config import config
from botocore.exceptions import ClientError
import os

#params = config('config.ini','aws')
#profile_name = params.get('profile')
#print(profile_name)

boto3.setup_default_session(profile_name='default')
s3_client = boto3.client('s3')
s3=boto3.resource('s3')
l_s3_bucket='pythonoct2022'

#for bucket in s3.buckets.all():
  # print(bucket.name)

for key in s3_client.list_objects(Bucket=l_s3_bucket)['Contents']:
    print(key['Key'])
	
#l_s3_bucket_resource = s3.Bucket(l_s3_bucket)
#for file in l_s3_bucket_resource.objects.all():
# print(file.key)