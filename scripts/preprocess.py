import os
import boto3
import re
import sagemaker

role = 'your-sagemaker-execution-role'
region = 'aws-region'

# S3 bucket for training data.
data_bucket = f"sagemaker-example-files-prod-{region}"
data_prefix = "datasets/tabular/uci_abalone"


# S3 bucket for saving code and model artifacts.
output_bucket = 'aws-s3-bucket-name'
output_prefix = "folder-name"

#Exploring Dataset
import boto3

s3 = boto3.client("s3")

FILE_TRAIN = "abalone_dataset1_train.csv"
FILE_TEST = "abalone_dataset1_test.csv"
FILE_VALIDATION = "abalone_dataset1_validation.csv"

# downloading the train, test, and validation files from data_bucket
s3.download_file(data_bucket, f"{data_prefix}/train_csv/{FILE_TRAIN}", FILE_TRAIN)
s3.download_file(data_bucket, f"{data_prefix}/test_csv/{FILE_TEST}", FILE_TEST)
s3.download_file(data_bucket, f"{data_prefix}/validation_csv/{FILE_VALIDATION}", FILE_VALIDATION)
s3.upload_file(FILE_TRAIN, output_bucket, f"{output_prefix}/train/{FILE_TRAIN}")
s3.upload_file(FILE_TEST, output_bucket, f"{output_prefix}/test/{FILE_TEST}")
s3.upload_file(FILE_VALIDATION, output_bucket, f"{output_prefix}/validation/{FILE_VALIDATION}")

import pandas as pd  # Read in csv and store in a pandas dataframe

df = pd.read_csv(
    FILE_TRAIN,
    sep=",",
    encoding="latin1",
    names=[
        "age",
        "sex",
        "Length",
        "Diameter",
        "Height",
        "Whole.weight",
        "Shucked.weight",
        "Viscera.weight",
        "Shell.weight",
    ],
)
print(df.head(1))

# creating the inputs for the fit() function with the training and validation location
s3_train_data = f"s3://{output_bucket}/{output_prefix}/train"
print(f"training files will be taken from: {s3_train_data}")
s3_validation_data = f"s3://{output_bucket}/{output_prefix}/validation"
print(f"validation files will be taken from: {s3_validation_data}")
output_location = f"s3://{output_bucket}/{output_prefix}/output"
print(f"training artifacts output location: {output_location}")
