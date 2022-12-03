'''
import json

# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                }"""

# Parse JSON using "loads" Method
y = json.loads(bill_json)

# Get Subset of JSON
print(y["BillDetails"])

# JSON Nested value, Get First Product
print(y["BillDetails"][0]["Product"])

# JSON Get All Products
for restaurant in y["BillDetails"]:
    print(restaurant["Product"])
'''

'''
import boto3

boto3.setup_default_session(profile_name='sb')
s3_client = boto3.client('s3')
s3=boto3.resource('s3')
l_s3_bucket='pythonoct2022'

for bucket in s3.buckets.all():
   print(bucket.name)

response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
'''
import s3_file_upload as s3u

l_s3_bucket='pythonoct2022'
ifilename = 'C:/Malini/Precision/codepractice/usa_cities_malini.csv'
objectname = 'incoming' 
print('before upload method')
s3u.upload_file(ifilename, l_s3_bucket, objectname)
print('after upload method')