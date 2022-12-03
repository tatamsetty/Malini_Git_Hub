#from fileinput import filename
#import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    print(file_name )
    print(bucket )
    print(object_name )
    # If S3 object_name was not specified, use file_name
    l_s3_file_name = ""
    if object_name is None:
        l_s3_file_name = os.path.basename(file_name)
    else:
        l_s3_file_name = object_name + "/" + os.path.basename(file_name)

    # Upload the file
    boto3.setup_default_session(profile_name='default')
    s3_client = boto3.client('s3')
    try:
        print(file_name )
        print(bucket )
        print(object_name )
        response = s3_client.upload_file(file_name, bucket, l_s3_file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    l_s3_bucket='pythonoct2022'
    ifilename = 'C:/Malini/Precision/codepractice/usa_cities_malini1.csv'
    objectname = 'incoming' 
    print('before upload method')
    upload_file(ifilename, l_s3_bucket, objectname)
    print('after upload method')

if __name__ == '__main__' :main()
'''
import boto3
from botocore.exceptions import ClientError
import os

#params = config('config.ini','aws)
#profile_name = params.get('profile')
boto3.setup_default_session(profile_name='default')
s3_client = boto3.client('s3')

def download_s3_file(p_s3_bucket_name,p_s3_folder,p_s3_file_name,p_local_download_folder_file):
   
    l_s3_file_path_name = p_s3_folder+"/"+p_s3_file_name
    s3_client.download_file(p_s3_bucket_name, l_s3_file_path_name, p_local_download_folder_file)
   
   
def upload_my_file(p_s3_bucket_name,p_s3_folder,p_local_folder_file_to_upload,p_upload_file_name= "N/A"):

    l_s3_file_name = ""
    if  p_upload_file_name == "N/A":
        l_s3_file_name = p_s3_folder + "/" + os.path.basename(p_local_folder_file_to_upload)
    else:
        l_s3_file_name = p_s3_folder + "/" + p_upload_file_name

    try:
        response = s3_client.upload_file(p_local_folder_file_to_upload,p_s3_bucket_name,l_s3_file_name)
    except ClientError as e:
        print(e)
        return False
    except FileNotFoundError as e:
        print(e)
        return False
    return True

def main():
    l_s3_bucket='pythonoct2022'
    l_s3_data_folder='retail_sales'
    l_s3_scripts_folder='scripts/db'
    l_local_folder_file_to_upload='C:/Malini/Precision/codepractice/usa_cities_malini.csv'
    l_file_name='rules_malini.csv'
    #Test 1
    upload_my_file(l_s3_bucket,l_s3_data_folder,l_local_folder_file_to_upload,l_file_name)
    #Test 2
    upload_my_file(l_s3_bucket,l_s3_data_folder,l_local_folder_file_to_upload)
        
   # download_s3_file(l_s3_bucket,l_s3_data_folder,"loan_rules.csv",'C:/Malini/Precision/codepractice/loan_rules_malini.csv')
if __name__ == '__main__' :main()
'''