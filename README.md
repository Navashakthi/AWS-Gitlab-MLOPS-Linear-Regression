# AWS-Gitlab-MLOPS-Linear-Regression
Automated ML workflow in AWS with Gitlab CI\CD and pipeline

This repository contains a GitLab CI/CD pipeline for automating the training and deployment of a machine learning model using Amazon SageMaker. The pipeline preprocesses data, trains a model, builds the model, configures and deploys a SageMaker endpoint, and finally runs inference tests.

## Prerequisites
Before running this pipeline, ensure you have the following prerequisites:

AWS Account: An active AWS account with permissions to use SageMaker, S3, and IAM services.
S3 Bucket: An S3 bucket where training data and model artifacts will be stored.
IAM Role: An IAM role with the necessary permissions for SageMaker to access S3 and other AWS resources such as ECR.
AWS CLI: AWS CLI configured with your access and secret keys, and the region set.
GitLab CI/CD: A GitLab project with CI/CD enabled and the environment variables set.

## Pipeline Stages

1. **Preprocess**
    - Downloads uci_abalone dataset and stores it in aws s3. Preprocesses the training data using a Python script preprocess.py.
    
2. **Train**
    - Creates a SageMaker training job using the preprocessed data and specified inbuilt algorithm linear learner algorithm.
    
3. **Build**
    - Builds the SageMaker model from the training job output artifacts and inbuilt algorithm image from AWS ECR.
    
4. **Config Deploy**
    - Configures the SageMaker endpoint with the built model from previous stage.
    
5. **Deploy**
    - Deploys the configured endpoint in SageMaker using deploy.py.
    
6. **Predict**
    - Runs inference tests using the deployed endpoint using predict.py.

## Environment Variables

Ensure the following environment variables are set in your GitLab CI/CD settings:

- `AWS_REGION`: Your AWS region.
- `AWS_S3_BUCKET`: S3 bucket name for storing data and model artifacts.
- `AWS_S3_PREFIX`: S3 prefix (folder name).
- `SAGEMAKER_ROLE`: SageMaker execution role ARN.
- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `AWS_LR_IMAGE`: URI of the built-in SageMaker Linear Learner algorithm image.
- `TRAINING_JOB_NAME`: Name for the SageMaker training job.
- `MODEL_NAME`: Name for the SageMaker model.
- `ENDPOINT_CONFIG_NAME`: Name for the SageMaker endpoint configuration.
- `ENDPOINT_NAME`: Name for the SageMaker endpoint.
