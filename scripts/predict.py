import json
import random
import boto3
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import JSONDeserializer

# Replace 'your-endpoint-name' with the actual endpoint name
endpoint_name = 'your-endpoint-name'

# Initialize the predictor
linear_predictor = Predictor(
    endpoint_name=endpoint_name,
    serializer=CSVSerializer(),
    deserializer=JSONDeserializer()
)

FILE_TEST = "your-s3-path-where-testdata-is-downloaded/test/abalone_dataset1_test.csv"

# Download the test file from S3
s3 = boto3.client('s3')
bucket_name, key = FILE_TEST.replace("s3://", "").split("/", 1)
local_file = "/tmp/test.csv"
s3.download_file(bucket_name, key, local_file)

# Read the testing sample from the test file
with open(local_file, "r") as file:
    test_data = file.readlines()

# Process each sample in the test data and get predictions
updated_test_data = []
for line in test_data:
    sample = line.strip().split(",")
    actual_age = sample[0]
    payload = sample[1:]  # Remove the actual age from the sample
    payload = ",".join(map(str, payload))

    # Invoke the predictor and analyze the result
    result = linear_predictor.predict(payload)

    # Extract the prediction value
    predicted_age = round(float(result["predictions"][0]["score"]), 2)

    # Add the predicted value to the line
    updated_line = line.strip() + f",{predicted_age}\n"
    updated_test_data.append(updated_line)

# Save the updated test data to the local file
updated_local_file = "/tmp/test_with_predictions.csv"
with open(updated_local_file, "w") as file:
    file.writelines(updated_test_data)

# Upload the updated file back to S3
updated_key = key.replace("test.csv", "test_with_predictions.csv")
s3.upload_file(updated_local_file, bucket_name, updated_key)

print(f"Updated test file with predictions saved to s3://{bucket_name}/{updated_key}")
