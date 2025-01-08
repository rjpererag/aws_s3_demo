import json
from botocore import client
from ..parsers.bucket import *


def validate_bucket_name(s3: client, bucket_name: str) -> bool:

    """
    Given a buket name verifies the existence of the bucket.

    return bool
    """

    buckets_raw = s3.list_buckets()
    buckets =parse_bucket(buckets_raw.get("Buckets"))

    return bucket_name in [b.name for b in buckets]


def validate_folder(contents: list[Content], folder_name):
    """
    Given a folder name verifies the existence inside a bucket.

    return bool
    """
    return folder_name not in [c.name for c in contents]


def list_bucket_contents(s3: client, bucket_name: str) -> list:
    
    if validate_bucket_name(s3=s3, bucket_name=bucket_name):
        contents_raw = s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in contents_raw:
            return parse_contents(contents_raw=contents_raw.get("Contents"))
        return []
    
    print("No bucket found")
    

def create_new_folder(s3: client, bucket_name: str, folder_name: str):

    try:
        if contents := list_bucket_contents(s3=s3, bucket_name=bucket_name):
            if validate_folder(contents=contents, folder_name=folder_name):
                response = s3.put_object(Bucket=bucket_name, Key=folder_name)
                return  f"Sucessfull creation for {folder_name}. ETag: {response.get("ETag")}" 
        
        return "No folder created"
    
    except Exception as e:
        print(f"Error creating {folder_name}. {str(e)}")


    


def put_object(s3: client,
               bucket_name: str,
               folder_name: str,
               file_name: str,
               data):

    try: 
        object_key = f'{folder_name}{file_name}'

        json_data = json.dumps(data)
        response = s3.put_object(Bucket=bucket_name, Key=object_key, Body=json_data)
        print( f"Sucessfull creation for {folder_name}. ETag: {response.get("ETag")}")
    
    except Exception as e:
        print(f"Error occurred creating th object in path: {object_key}. {str(e)}")

