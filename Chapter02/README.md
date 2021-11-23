# Chapter 2
In this chapter, we learned about the foundational architectural concepts that are typically applied when designing real-life analytics data management and processing solutions. We also discussed three analytics data management architectures that you would find most commonly used across organizations today: data warehouse, data lake, and data lakehouse.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter we installed the AWS Command Line Interface (CLI) tool, and used the AWS CLI to create a new Amazon S3 bucket. 

### Links
- **AWS CLI download:** https://aws.amazon.com/cli/
- **Learn more about S3 bucket naming rules:** https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html

### Commands
#### Create a new Amazon S3 bucket
The following command creates a new bucket called *dataeng-test-bucket-123*. If a bucket with this name already exists the command will fail, so you need to ensure you provide a globally unique name.  

```
aws s3 mb s3://dataeng-test-bucket-123
```
