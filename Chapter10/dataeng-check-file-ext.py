import urllib.parse
import os
import json
print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    bucket = event['detail']['requestParameters']['bucketName']
    key = urllib.parse.unquote_plus(event['detail']['requestParameters']['key'], encoding='utf-8')
    filename, file_extension = os.path.splitext(key)
    print(f'File extension is: {file_extension}')
    payload = {
        "file_extension": file_extension,
        "bucket": bucket,
        "key": key
        }
    return payload
