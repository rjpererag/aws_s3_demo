import boto3
import json
from dataclasses import asdict
from src.utils.bucket import *
from decouple import config


def main():
    bucket_name = config("BUCKET_NAME")
    folder_name = config("FOLDER_NAME")
    new_folder_name = config("NEW_FOLDER_NAME")
    file_name = config("FILE_NAME")
    
    # Creating client
    s3 = boto3.client("s3")

    # To verify the existence of the bucket
    is_valid_bucket_name = validate_bucket_name(
        s3=s3, bucket_name=bucket_name)

    # To list bucket content (already handles validation)
    bucket_contents = list_bucket_contents(
        s3=s3, bucket_name=bucket_name)

    # To validate fodler
    is_valid_folder = validate_folder(
        contents=bucket_contents, folder_name=folder_name)
    
    # To create new folder
    creation_response = create_new_folder(
        s3=s3, bucket_name=bucket_name, folder_name=new_folder_name)
    

    final_response = {
        "is_valid_bucket_name": is_valid_bucket_name,
        "is_valid_folder": is_valid_folder,
        "creation_response": creation_response
    }
    
    json_data = json.dumps(final_response)
    print(json_data)
    print("-------------------------------------------------")
    put_object(s3=s3,
               bucket_name=bucket_name,
               folder_name=new_folder_name,
               file_name=file_name,
               data=json_data)
    

if __name__ == "__main__":
    main()

