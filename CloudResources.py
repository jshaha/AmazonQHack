"""
Cloud-based Tic-tac-toe Game
AWS Resource Management
"""
import boto3
import time
import re


class CloudResources:
    def __init__(self, region='us-west-2'):
        """Initialize AWS clients"""
        self.s3 = boto3.client('s3', region_name=region)
        self.dynamodb = boto3.client('dynamodb', region_name=region)
        self.region = region

   

    def create_s3_bucket(self, move):
        """
        Create an S3 bucket for the given move.
        The bucket name will include the sanitized move string.
        """
        # Sanitize move string
        sanitized_move = re.sub(r'[^a-z0-9-]', '-', move.lower())  # Replace invalid characters with hyphen
        sanitized_move = sanitized_move.strip('-')  # Ensure it doesn't start or end with a hyphen

        # Construct the bucket name
        bucket_name = f"tictactoe-{sanitized_move}-{int(time.time())}"

        # Ensure the name is within 63 characters
        if len(bucket_name) > 63:
            bucket_name = bucket_name[:63]

        try:
            if self.region == "us-east-1":
                self.s3.create_bucket(Bucket=bucket_name)
            else:
                self.s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.region}
                )
            print(f"Created S3 bucket: {bucket_name}")
        except Exception as e:
            print(f"Error creating S3 bucket: {e}")


    def create_database(self, name):
        table_name = f"tictactoe-{name}-{int(time.time())}"
        try:
            self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[{'AttributeName': 'MoveID', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'MoveID', 'AttributeType': 'S'}],
                BillingMode='PAY_PER_REQUEST'
            )
            print(f"Created DynamoDB table: {table_name}")
        except Exception as e:
            print(f"Error creating DynamoDB table: {e}")

    def cleanup_resources(self):
        
        try:
            # Cleanup S3 buckets
            response = self.s3.list_buckets()
            for bucket in response['Buckets']:
                if bucket['Name'].startswith("tictactoe"):
                    print(f"Deleting bucket: {bucket['Name']}")
                    # Delete all objects in the bucket before deleting the bucket
                    objects = self.s3.list_objects_v2(Bucket=bucket['Name'])
                    if 'Contents' in objects:
                        for obj in objects['Contents']:
                            self.s3.delete_object(Bucket=bucket['Name'], Key=obj['Key'])
                    self.s3.delete_bucket(Bucket=bucket['Name'])

            # Cleanup DynamoDB tables
            response = self.dynamodb.list_tables()
            for table in response['TableNames']:
                if table.startswith("tictactoe"):
                    print(f"Deleting table: {table}")
                    waiter = self.dynamodb.get_waiter('table_exists')
                    waiter.wait(TableName=table)  # Wait for the table to be ACTIVE
                    self.dynamodb.delete_table(TableName=table)
        except Exception as e:
            print(f"Error during cleanup: {e}")

