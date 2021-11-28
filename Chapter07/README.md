# Chapter 7 - Transforming Data to Optimize for Analytics

In this chapter, we reviewed a number of common transformations that can be applied
to raw datasets, covering both generic transformations used to optimize data for analytics,
and business transforms used to enrich and denormalize datasets.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we joined various datasets that we had previously ingested in order to denormalize the underlying datasets. We then joined data we had ingested from a database with data that had been streamed into the data lake.

#### Creating a new data lake zone – the curated zone
- AWS Management Console - S3: - AWS Management Console - S3: https://s3.console.aws.amazon.com/s3/home

#### Creating a new IAM role for the Glue job
- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies

- AWS IAM policy for `DataEngGlueCWS3CuratedZoneWrite`. Change *INITIALS* in the policy below to match the name of the relevant bucket that you previously created.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::dataeng-landing-zone-INITIALS/*",
                "arn:aws:s3:::dataeng-clean-zone-INITIALS/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": "arn:aws:s3:::dataeng-curated-zone-INITIALS/*"
        }
    ]
}
```


