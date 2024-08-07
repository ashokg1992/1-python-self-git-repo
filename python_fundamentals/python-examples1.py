
# ======= 1-ec2 creation example ========================
import boto3

# Configure AWS credentials (replace with your actual credentials)
access_key_id = "YOUR_ACCESS_KEY_ID"
secret_access_key = "YOUR_SECRET_ACCESS_KEY"
region_name = "YOUR_REGION_NAME"  # e.g., "us-east-1"

# Create a boto3 EC2 client
ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region_name
)

# Define the EC2 instance configuration
image_id = "ami-0123456789abcdef0"  # Replace with the desired AMI ID
instance_type = "t2.micro"  # Choose the appropriate instance type
count = 1  # Number of instances to create

# Create the EC2 instance(s)
try:
  response = ec2_client.run_instances(
      ImageId=image_id,
      InstanceType=instance_type,
      MinCount=count,
      MaxCount=count
  )

  # Print instance information
  for instance in response["Instances"]:
      print(f"Instance ID: {instance['InstanceId']}")
      print(f"State: {instance['State']['Name']}")
      print("-" * 20)

except Exception as e:
  print(f"Error creating EC2 instance: {e}")
  
  
# =========================================================


# ==================== 1-s3 listing-s3-objects====================== 

import boto3# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
    
    
#  ========================================================
