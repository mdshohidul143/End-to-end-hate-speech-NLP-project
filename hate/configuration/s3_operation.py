import os

class S3Operation:

    def sync_folder_to_s3(self, s3_bucket_name, filepath, filename):

        command = f"aws s3 cp {filepath}/{filename} s3://{s3_bucket_name}/"
        os.system(command)

    def sync_folder_from_s3(self, s3_bucket_name, filename, destination):

        command = f"aws s3 cp s3://{s3_bucket_name}/{filename} {destination}/{filename}"
        os.system(command)
