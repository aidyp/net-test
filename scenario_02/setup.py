import boto3
import os
import sys

if "SETUP_COMPLETED" in os.environ:
    print("You've already run this setup. If you want it again, clear the SETUP_COMPLETED environment variable")
    sys.exit(0)

ec2 = boto3.resource('ec2')

# Launch instance into known subnet from the EC2 instance

ec2.create_instances(ImageId='ami-0c2b8ca1dad447f8a', )

