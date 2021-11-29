# Chapter 11 - Ad-hoc queries with Amazon Athena

Amazon Athena is a serverless, fully managed service that lets you use SQL to directly query data in the data lake, as well as query various other databases. It requires no setup, and the cost is based purely on the amount of data that is scanned to complete the query.  

In this chapter, we did a deep dive into Athena, examining how Athena can be used to query data directly in the data lake, query data from other data sources with Query Federation, and how Athena provides workgroup functionality to help with governance and cost management.

## Hands-on Activity

In the hands-on activity section of this chapter, we're going to create and configure a new Athena Workgroup and learn more about how Workgroups can help separate groups of users.

#### Creating an Amazon Athena workgroup and configuring Athena settings

- AWS Management Console - Amazon Athena: https://console.aws.amazon.com/athena

#### Switching Workgroups and running queries

- AWS Documentation on IAM Policies for Accessing Workgroups: https://docs.aws.amazon.com/athena/latest/ug/workgroups-iampolicy.html

- Query to determine most popular category of films (Step 3)
```
SELECT category_name, count(category_name) streams
FROM streaming_films
GROUP BY category_name
ORDER BY streams DESC
```

- Query to determine which State streamed the most films (Step 6)
```
SELECT state, count(state) count
FROM streaming_films
GROUP BY state
ORDER BY count desc
```






