# Chapter 6 - Ingesting Batch and Streaming Data

In this chapter, we discussed the 5 V's of data (volume, velocity, variety, validity, and value). 
We then reviewed a few different approaches for ignesting data from databases, and from streaming data sources.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we firstly used Amazon Database Migration Service (DMS) to ingest data from a MySQL database, and then we configured Amazon Kinesis Data Firehose to ingest streaming data that we generated using Amazon Kinesis Data Generator (KDG).

### Ingesting data with Amazon DMS

#### Creating a MySQL database instance
- AWS Management Console - RDS: https://console.aws.amazon.com/rds/home

#### Loading the demo database using an Amazon EC2 instance

- User data that is specified for the EC2 instance, to load data to the RDS database. **Change** the *HOST* and *PASSWORD* below to match your RDS instance host name and the password you set when creating the RDS instance.

```
#!/bin/bash
yum install -y mariadb
curl https://downloads.mysql.com/docs/sakila-db.zip -o sakila.zip
unzip sakila.zip
cd sakila-db
mysql --host=HOST --user=admin --password=PASSWORD -f < sakila-schema.sql
mysql --host=HOST --user=admin --password=PASSWORD -f < sakila-data.sql
```

#### Creating an IAM policy and role for DMS

- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies

- AWS IAM policy for `DataEngDMSLandingS3BucketPolicy`. **Change** INITIALS in the policy below to match the name of the landing zone bucket that you previously created. 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::dataeng-landing-zone-INITIALS",
                "arn:aws:s3:::dataeng-landing-zone-INITIALS/*"
            ]
        }
    ]
}
```

#### Querying data with Amazon Athena
- Athena query to validate that data has been successfully ingested using DMS  
`select * from film limit 20;`

- Further reading: [Using Amazon S3 as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)

- Further reading: [Using a MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html)

### Ingesting Streaming Data

#### Configuring Kinesis Data Firehose for streaming delivery to Amazon S3
- *S3 Bucket Prefix* for Kinesis Data Firehose: `streaming/!{timestamp:yyyy/MM/}`
- *S3 Bucket Error Output Prefix* for Kinesis Data Firehose: `!{firehose:error-output-type}/!{timestamp:yyyy/MM/}`

#### Configuring Amazon Kinesis Data Generator (KDG)

- Record template for Kinesis Data Generator
```
{
    "timestamp":"{{date.now}}",
    "eventType":"{{random.weightedArrayElement(
        {
            "weights": [0.3,0.1,0.6],
            "data": ["rent","buy","trailer"]
        }
    )}}",
    "film_id":{{random.number(
    {
        "min":1,
        "max":1000
    }
    )}},
    "distributor":"{{random.arrayElement(
        ["amazon prime", "google play", "apple itunes","vudo", "fandango now", "microsoft", "youtube"]
    )}}",
    "platform":"{{random.arrayElement(
        ["ios", "android", "xbox", "playstation", "smarttv", "other"]
    )}}",
    "state":"{{address.state}}"
}
```

#### Querying data with Amazon Athena
- Athena query to validate that data has been successfully ingested using DMS  
`select * from streaming limit 20;`




