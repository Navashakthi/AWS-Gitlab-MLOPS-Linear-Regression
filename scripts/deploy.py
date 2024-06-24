import boto3
import argparse
import sagemaker
from sagemaker.model import Model

# Define your bucket and paths
bucket_name = 'aws-s3-bucket-name'
output_prefix = 'folder-name'
model_artifact_path = "path-to-output-training-job/output/model.tar.gz"
role = 'sagemaker-execution-role'

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Create a SageMaker model
model = Model(
    model_data=model_artifact_path,
    role=role,
    image_uri='inbuilt-linear-learner-image-uri',
    sagemaker_session=sagemaker_session
)

# Deploy the model to an endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.c4.xlarge'
)

# Output the endpoint name
print(f"\nCreated endpoint")
