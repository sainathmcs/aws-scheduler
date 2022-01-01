import boto3
import json

payload = {
    "payload": "hi",
    "date": "2021-10-03T17:14:01",
    "target": "arn:aws:sns:ap-south-1:561707240222:scheduler-output-v2-dev",
    "user": "arn:aws:iam::561707240222:role/aws-scheduler-v2-dev-ap-south-1-lambdaRole"
}

boto3.client("sns").publish(
    TopicArn= "arn:aws:sns:ap-south-1:561707240222:scheduler-input-v2-dev",
    Message= json.dumps(payload)
)