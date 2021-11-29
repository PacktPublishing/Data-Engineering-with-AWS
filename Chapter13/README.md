# Chapter 13 - Enabling Artificial Intelligence and Machine Learning

In this chapter, you learned more about the broad range of AWS ML and AI services
and had the opportunity to get hands-on with Amazon Comprehend, an AI service for
extracting insights from written text.  

We discussed how ML and AI services can apply to a broad range of use cases, both
specialized (such as detecting cancer early) and general (business forecasting or
personalization).  

We examined different AWS services related to ML and AI. We looked at how different
Amazon SageMaker capabilities can be used to prepare data for ML, build models, train
and fine-tune models, and deploy and manage models. SageMaker makes building custom
ML models much more accessible to developers without existing expertise in ML.  

We then looked at a range of AWS AI services that provide prebuilt and trained models for
common use cases. We looked at services for transcribing text from audio files (Amazon
Transcribe), for extracting text from forms and handwritten documents (Amazon
Textract), for recognizing images (Amazon Rekognition), and for extracting insights from
text (Amazon Comprehend). We also briefly discussed other business-focused AI services,
such as Amazon Forecast and Amazon Personalize.

## Hands-on Activity
In the hands-on acitvity section of this chapter we looked at how we can use the ***Amazon Comprehend*** service to gain insight into the sentiment of reviews posted to a website. We configured an SQS queue to receive the details of newly posted reviewes, and had a Lambda function configured to pass the review text to Amazon Comprehend to gain insight into the review sentiment (postivie, negative, or netural). 

#### Setting up a new Amazon SQS message queue

- Amazon Management Console - SQS: https://console.aws.amazon.com/sqs/v2/.

#### Creating a Lambda function for calling Amazon Comprehend

- Amazon Management Console - Lambda: https://console.aws.amazon.com/lambda/






