# AWS-Gitlab-MLOPS-Linear-Regression
Automated ML workflow in AWS with Gitlab CI\CD and pipeline

This repository contains a GitLab CI/CD pipeline for automating the training and deployment of a machine learning model using Amazon SageMaker. The pipeline preprocesses data, trains a model, builds the model, configures and deploys a SageMaker endpoint, and finally runs inference tests.

## Prerequisites
Before running this pipeline, ensure you have the following prerequisites:

- **AWS Account**: An active AWS account with permissions to use SageMaker, S3, and IAM services.
- **S3 Bucket:** An S3 bucket where training data and model artifacts will be stored.
- **IAM Role:** An IAM role with the necessary permissions for SageMaker to access S3 and ECR.
- **AWS CLI:** AWS CLI configured with your access and secret keys, and the region set.
- **GitLab CI/CD:** A GitLab project with CI/CD enabled and the environment variables set mentioned below.


## Pipeline Stages

1. **Preprocess** : Downloads uci_abalone dataset and stores it in aws s3. Preprocesses the training data using a Python script preprocess.py.
2. **Train** : Creates a SageMaker training job using the preprocessed data and specified inbuilt algorithm linear learner algorithm.
3. **Build** : Builds the SageMaker model from the training job output artifacts and inbuilt algorithm image from AWS ECR.
4. **Config Deploy** : Configures the SageMaker endpoint with the built model from previous stage.
5. **Deploy** : Deploys the configured endpoint in SageMaker using deploy.py.
6. **Predict** : Runs inference tests using the deployed endpoint using predict.py.

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

## How to Execute the Pipeline

Follow these steps to execute the entire CI/CD pipeline:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Environment Variables**:
   - In your GitLab project, navigate to **Settings** > **CI/CD** > **Variables**.
   - Add the required environment variables with appropriate values

3. **Prepare the Data and Scripts**:
   - Ensure you have the necessary training data in your S3 bucket.
   - Create the preprocessing, training, and prediction scripts in the `scripts` directory.

4. **Review the `.gitlab-ci.yml` File**:
   - Verify the pipeline stages and commands in the `.gitlab-ci.yml` file.
   - Make sure the paths and commands match your project structure and requirements.

5. **Push to GitLab**:
   - Commit and push your changes to GitLab:
     ```bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```

6. **Monitor the Pipeline**:
   - Navigate to your GitLab project and go to **CI/CD** > **Pipelines**.
   - Monitor the progress of your pipeline stages: preprocess, train, build, config_deploy, deploy, predict, and cleanup.

7. **Verify the Results**:
   - Once the pipeline execution is complete, verify that the SageMaker endpoint is created and the inference tests are successful.
   - Check that the resources are deleted after the cleanup stage to ensure cost savings.

By following these steps, you can execute the entire CI/CD pipeline to automate the training and deployment of a machine learning model using Amazon SageMaker with GitLab CI/CD.

## After Work

To manage costs effectively, especially after project completion or pipeline execution, include a cleanup job in your pipeline to delete resources that are no longer needed. This ensures that you are not incurring charges for idle or unused resources.

### Cleanup Job

Add a cleanup stage to your `.gitlab-ci.yml` file to delete the SageMaker endpoint, model, and other resources:

```yaml
stages:
  - preprocess
  - train
  - build
  - config_deploy
  - deploy
  - predict
  - cleanup

# Other stages ...

cleanup:
  stage: cleanup
  image: python:3.8
  script:
    - aws sagemaker delete-endpoint --endpoint-name $ENDPOINT_NAME
    - aws sagemaker delete-endpoint-config --endpoint-config-name $ENDPOINT_CONFIG_NAME
    - aws sagemaker delete-model --model-name $MODEL_NAME
    - aws s3 rm s3://$AWS_S3_BUCKET/$AWS_S3_PREFIX/ --recursive
    - echo "Resources deleted to save costs."
  only:
    - schedules
    - manual
```

### Explanation

- **Stage Addition**: The `cleanup` stage is added to the pipeline.
- **Delete Commands**: AWS CLI commands are used to delete the SageMaker endpoint, endpoint configuration, model, and S3 bucket contents.
- **Trigger Conditions**: The cleanup job can be triggered manually or through scheduled runs to ensure resources are deleted after the project is completed or periodically to avoid unnecessary costs.

By incorporating this cleanup stage, you ensure that resources are properly managed and costs are minimized once the pipeline execution or project is completed.

## Future Work

- **Environment Variables Best Practices**: Follow best practices for managing environment variables, such as using GitLab's CI/CD variable masking and secret management features.
- **Parameter Management**: Refactor the pipeline and scripts to dynamically retrieve and use parameters such as S3 paths, model names, model output, and endpoint names directly from the pipeline environment variables.
- **Modular Python Scripts**: Update Python scripts to accept parameters via command-line arguments or environment variables for better integration with the pipeline.
- **Enhanced Logging and Monitoring**: Integrate logging and monitoring solutions to track the status and performance of the pipeline and deployed models.
- **Automated Testing**: Add automated tests for each stage of the pipeline to ensure data integrity and model accuracy throughout the process.
