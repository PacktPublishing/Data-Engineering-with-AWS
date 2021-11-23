# Chapter 3
In this chapter we reviewed a range of AWS services at a high level, including services for ingesting data from a variety of sources, services for transforming data, and services for consuming and working with data.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we configured an S3 bucket to automatically trigger a Lambda function whenever a new CSV file was written to the bucket. In the Lambda function, we used an open-source library to convert the CSV file into Parquet format, and wrote the file out to a new zone of our data lake.

#### Creating a Lambda layer containing the AWS Data Wrangler library
- AWS Data Wrangler GitHub site: https://github.com/awslabs/aws-data-wrangler

  - AWS Data Wrangler v2.10 ZIP file for Python 3.8: https://github.com/awslabs/aws-data-wrangler/releases/download/2.10.0/awswrangler-layer-2.10.0-py3.8.zip
- AWS Management Console - Lambda Layers: https://console.aws.amazon.com/lambda/home#/layers

#### Creating new Amazon S3 buckets
- AWS Management Console - S3: https://s3.console.aws.amazon.com/s3/home

#### Creating an IAM policy and role for your Lambda function
- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies
- Policy JSON for `DataEngLambdaS3CWGluePolicy`: 

#### Creating a Lambda function
- AWS Management Console - Lambda Functions: https://console.aws.amazon.com/lambda/home#/functions
- `CSVtoParquetLambda` function code:

#### Configuring our Lambda function to be triggered by an S3 upload
- Sample CSV file: 
- Command to upload file to S3:   

*Ensure you replace INITIALS below to reflect the name of the bucket you previously created*

```
aws s3 cp test.csv s3://dataeng-landing-zone-INITIALS/testdb/csvparquet/test.csv
```
- Command to list the newly created Parquet files in the clean-zone bucket: 

*Ensure you replace INITIALS below to reflect the name of the bucket you previously created*

```
aws s3 ls s3://dataeng-clean-zone-initials/testdb/csvparquet/
```
  

