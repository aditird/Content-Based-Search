import boto3

# Initialize AWS Rekognition client
rekognition_client = boto3.client('rekognition', region_name='us-east-2')

def detect_labels(image_s3_bucket, image_s3_key):
    """
    Detect labels in the image using AWS Rekognition.
    """
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': image_s3_bucket,
                'Name': image_s3_key
            }
        },
        MaxLabels=10,  # Max labels to detect
        MinConfidence=70  # Minimum confidence level for labels
    )
    return response['Labels']

def detect_text(image_s3_bucket, image_s3_key):
    """
    Detect text in the image using AWS Rekognition.
    """
    response = rekognition_client.detect_text(
        Image={
            'S3Object': {
                'Bucket': image_s3_bucket,
                'Name': image_s3_key
            }
        }
    )
    return response['TextDetections']
