# AWS-Gitlab-MLOPS-Linear-Regression
Automated ML workflow in AWS with Gitlab CI\CD and pipeline
# SageMaker GitLab CI/CD Pipeline

This repository contains a GitLab CI/CD pipeline for automating the training and deployment of a machine learning model using Amazon SageMaker. The pipeline preprocesses data, trains a model, builds the model, configures and deploys a SageMaker endpoint, and finally runs inference tests.

## Pipeline Stages

1. **Preprocess**
    - Preprocesses the training data using a Python script.
    
2. **Train**
    - Creates a SageMaker training job using the preprocessed data and specified algorithm.
    
3. **Build**
    - Builds the SageMaker model from the training job output.
    
4. **Config Deploy**
    - Configures the SageMaker endpoint with the built model.
    
5. **Deploy**
    - Deploys the configured endpoint in SageMaker.
    
6. **Predict**
    - Runs inference tests using the deployed endpoint.

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
