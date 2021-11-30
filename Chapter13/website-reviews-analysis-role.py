import boto3
import json
comprehend = boto3.client(service_name='comprehend', 
                region_name='us-east-2')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        print(str(payload))

        print('Calling DetectSentiment')
        response = comprehend.detect_sentiment(Text=payload,
                    LanguageCode='en')
        sentiment = response['Sentiment']
        sentiment_score = response['SentimentScore']
        print(f'SENTIMENT: {sentiment}')
        print(f'SENTIMENT SCORE: {sentiment_score}')

        print('Calling DetectEntities')
        response = comprehend.detect_entities(Text=payload,
                    LanguageCode='en')
        #print(response['Entities'])
        for entity in response['Entities']: 
            entity_text = entity['Text']
            entity_type = entity['Type']
            print(
                f'ENTITY: {entity_text}, '
                f'ENTITY TYPE: {entity_type}'
                )
    return
