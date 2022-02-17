# Chapter 3 - The AWS Data Engineers Toolkit
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
- Policy JSON for `DataEngLambdaS3CWGluePolicy`: [DataEngLambdaS3CWGluePolicy](DataEngLambdaS3CWGluePolicy.json)  
  [Ensure you replace INITIALS in the policy statements to reflect the name of the S3 buckets you created]

#### Creating a Lambda function
- AWS Management Console - Lambda Functions: https://console.aws.amazon.com/lambda/home#/functions
- `CSVtoParquetLambda` function code: [CSVtoParquetLambda.py](CSVtoParquetLambda.py)  
 **Note:** Make sure you don't miss the step about increasing the Lambda function timeout to 1 minute (Step 10 on Page 93 of the printed book). If using a larger CSV file than the file provided here as a sample (test.csv) then consider also increasing the memory allocation. 

#### Configuring our Lambda function to be triggered by an S3 upload
- Sample CSV file: [test.csv](test.csv)

##### Command to upload file to S3:
**Note:** In the original version of this exercise (as shown in the print edition of the book on Page 95), the path below was `dataeng-landing-zone-INITIALS/testdb/csvaprquet/test.csv`. However, in Chapter 4 when querying the database/table that gets created by this step, we refer to the database as `cleanzonedb`. The path of the upload determines the name of the database/table, which is why you should use `cleanzonedb` as shown below, rather than `testdb` as in the original version of this exercise. *Many thanks to the reader that noticed this and let us know about the mismatch!*

###### Ensure you replace INITIALS below to reflect the name of the bucket you previously created

```
aws s3 cp test.csv s3://dataeng-landing-zone-INITIALS/cleanzonedb/csvparquet/test.csv
```
##### Command to list the newly created Parquet files in the clean-zone bucket: 
###### Ensure you replace INITIALS below to reflect the name of the bucket you previously created

```
aws s3 ls s3://dataeng-clean-zone-INITIALS/cleanzonedb/csvparquet/
```
  

