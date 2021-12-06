# Data Engineering with AWS

<a href="https://www.packtpub.com/product/data-engineering-with-aws/9781800560413"><img src="https://static.packt-cdn.com/products/9781800560413/cover/smaller" alt="Data Engineering with AWS" height="256px" align="right"></a>

This is the code repository for [Data Engineering with AWS](https://www.packtpub.com/product/data-engineering-with-aws/9781800560413), published by Packt.

**Learn how to design and build cloud-based data transformation pipelines using AWS**

## What is this book about?

Knowing how to architect and implement complex data pipelines is a highly sought-after skill. Data engineers are responsible for building these pipelines that ingest, transform, and join raw datasets - creating new value from the data in the process.

Amazon Web Services (AWS) offers a range of tools to simplify a data engineer's job, making it the preferred platform for performing data engineering tasks.
This book will take you through the services and the skills you need to architect and implement data pipelines on AWS. You'll begin by reviewing important data engineering concepts and some of the core AWS services that form a part of the data engineer's toolkit. You'll then architect a data pipeline, review raw data sources, transform the data, and learn how the transformed data is used by various data consumers. The book also teaches you about populating data marts and data warehouses along with how a data lakehouse fits into the picture. Later, you'll be introduced to AWS tools for analyzing data, including those for ad-hoc SQL queries and creating visualizations. In the final chapters, you'll understand how the power of machine learning and artificial intelligence can be used to draw new insights from data.

By the end of this AWS book, you'll be able to carry out data engineering tasks and implement a data pipeline on AWS independently.

This book covers the following exciting features: 
* Understand data engineering concepts and emerging technologies
* Ingest streaming data with Amazon Kinesis Data Firehose
* Optimize, denormalize, and join datasets with AWS Glue Studio
* Use Amazon S3 events to trigger a Lambda process to transform a file
* Run complex SQL queries on data lake data using Amazon Athena
* Load data into a Redshift data warehouse and run queries
* Create a visualization of your data using Amazon QuickSight
* Extract sentiment data from a dataset using Amazon Comprehend

If you feel this book is for you, get your [copy](https://www.amazon.in/Data-Engineering-AWS-cloud-based-transformation/dp/1800560419/ref=sr_1_3?keywords=Data+Engineering+with+AWS&qid=1638757232&sr=8-3) today!

<a href="https://www.packtpub.com/product/data-engineering-with-aws/9781800560413"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
import boto3
import awswrangler as wr
from urllib.parse import unquote_plus
```
**Following is what you need for this book:**
This book is for data engineers, data analysts, and data architects who are new to AWS and looking to extend their skills to the AWS cloud. Anyone who is new to data engineering and wants to learn about the foundational concepts while gaining practical experience with common data engineering services on AWS will also find this book useful.
A basic understanding of big data-related topics and Python coding will help you get the most out of this book but is not needed. Familiarity with the AWS console and core services is also useful but not necessary.

With the following software and hardware list you can run all code files present in the book (Chapter 1-14).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  	1-14	   |   	AWS Web Services(AWS) with a recent version of a modern web browser(Chrome, Edge, etc.)                                  			  | Any OS | 		

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800560413_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Serverless Analytics with Amazon Athena  [[Packt]](https://www.packtpub.com/product/serverless-analytics-with-amazon-athena/9781800562349) [[Amazon]](https://www.amazon.in/Serverless-Analytics-Amazon-Athena-semi-structured/dp/1800562349/ref=sr_1_1?keywords=Serverless+Analytics+with+Amazon+Athena&qid=1638757768&sr=8-1)
  
* Scalable Data Streaming with Amazon Kinesis  [[Packt]](https://www.packtpub.com/product/scalable-data-streaming-with-amazon-kinesis/9781800565401) [[Amazon]](https://www.amazon.in/Scalable-Data-Streaming-Amazon-Kinesis/dp/1800565402/ref=sr_1_1?keywords=Scalable+Data+Streaming+with+Amazon+Kinesis&qid=1638757818&sr=8-1)
  
## Get to Know the Author
**Gareth Eagar** has worked in the IT industry for over 25 years, starting in South Africa, then working in the United Kingdom, and now based in the United States. In 2017, he started working at Amazon Web Services (AWS) as a solution architect, working with enterprise customers in the NYC metro area. Gareth has become a recognized subject matter expert for building data lakes on AWS, and in 2019 he launched the Data Lake Day educational event at the AWS Lofts in NYC and San Francisco. He has also delivered a number of public talks and webinars on topics relating to big data, and in 2020 Gareth transitioned to the AWS Professional Services organization as a senior data architect, helping customers architect and build complex data pipelines.

**Note from the author:**

You can use the resources provided in this GitHub repo as you work through the hands-on activities includes in each chapter of the book. This repo is laid out with resources matched to each chapter of the book - such as the JSON used to define IAM policies, sample files, relevant links, etc. 
