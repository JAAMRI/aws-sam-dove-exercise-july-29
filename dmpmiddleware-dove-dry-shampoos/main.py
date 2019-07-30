import json

# import requests


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from dmpmiddleware-dove-dry-shampoos-function",
            # "location": ip.text.replace("\n", "")
        }),
    }
