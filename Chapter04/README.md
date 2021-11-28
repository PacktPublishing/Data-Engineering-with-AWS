# Chapter 4 - Data Cataloging, Security, and Governance

In this chapter, we reviewed important concepts around data security and governance, including how a data catalog can be used to help prevent your data lake from becoming a data swamp.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we created a new data lake user and assigned them permissions using AWS Identitty and Access Management (IAM). Once we verified their permissions, we then transitioned data authorization over to use Lake Formation for fine-grained access control (including the ability to control permissions at the column level). 

#### Creating a new user with IAM permissions
- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies

- Resource section of policy that is updated to limit access to just the Glue `cleanzonedb` database and tables in that database
```
            "Resource": [
                "arn:aws:glue:*:*:catalog",
                "arn:aws:glue:*:*:database/cleanzonedb",
                "arn:aws:glue:*:*:database/cleanzonedb*",
                "arn:aws:glue:*:*:table/cleanzonedb/*"
            ]
```

- New section of policy that enables access to the underlying S3 storage for the `cleanzonedb` database. Ensure that you modify INITIALS below to reflect the correct name for your CleanZoneDB bucket
```
       {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:ListMultipartUploadParts",
                "s3:AbortMultipartUpload",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::dataeng-clean-zone-INITIALS/*"
            ]
        },
```

- Athena query to validate that IAM permissions are correct for the datalake-user:
`select * from cleanzonedb.csvparquet`

#### Transitioning to managing fine-grained permissions with AWS Lake Formation

- AWS Management Console - Lake Formation: https://console.aws.amazon.com/lakeformation/home

