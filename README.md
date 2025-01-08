# AWS S3 DEMO

This demo illustrates several ways to interact with S3 buckets to perform the following actions:

- Validate buckets names: To check the existence of a bucket by its name
- Validate folder: To check the existence of a folder witihin a specific bucket
- List bucket contents: To display the name of every object witihin the bucket
- Create new folder: To create a new folder witihin a specific bucket by first validating bucket and folder existence
- Upload object: to put a new object inside an specific bucket and folder

## How to use it

To reuse the code we must establish the ENV variables:
- BUCKET_NAME
- FOLDER_NAME
- NEW_FOLDER_NAME
- FILE_NAME