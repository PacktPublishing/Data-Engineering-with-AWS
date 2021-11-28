# Chapter 9 - Loading Data into a Data Mart

In this chapter, we learned how a cloud data warehouse can be used to store hot data to
optimize performance and manage costs. We reviewed some common "anti-patterns"
for data warehouse usage before diving deep into the Redshift architecture to learn more
about how Redshift optimizes data storage across nodes.
We then reviewed some of the important design decisions that need to be made when
creating an optimized schema in Redshift, before reviewing ingested unloaded from
Redshift.

## Hands-on Activity
In the hands-on section of this chapter we created a new Redshift cluster,
configured Redshift Spectrum to query data from Amazon S3, and then loaded a
subset of data from S3 into Redshift. We then ran some complex queries to calculate the
distance between two points before creating a materialized view with the results of our
complex query.

#### Uploading our sample data to Amazon S3
In this exercise, we use open-source data from an organization called **Inside Airbnb** that provides data that quantifies the impact of short-term rentals on housing and residential communities. To learn more about the organization, see http://insideairbnb.com/index.html.

The following links are to download data from [*Inside Airbnb*](http://insideairbnb.com/index.html), who have licensed this data under [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

Download the ***listings.csv*** file for Jersey City, New Jersey, and for New York City, New York, using the following links. *Make sure to download the CSV version of the file, and not the csv.gz version*. Rename each file when downloading so you can identify which city it is for (such as jc-listings.csv and ny-listings.csv). 

- Jersey City Listings: [Access here](http://insideairbnb.com/get-the-data.html#:~:text=Jersey%20City%2C%20New%20Jersey%2C%20United%20States)
- New York Listings: [Access here](http://insideairbnb.com/get-the-data.html#:~:text=New%20York%20City%2C%20New%20York%2C%20United%20States)

**Commands to upload files to Amazon S3**  

- Use the following commands to upload the data to your S3 Landing Zone bucket  
```
aws s3 cp jc-listings.csv s3://dataeng-landing-zone-INITIALS/listings/city=jersey_city/jc-listings.csv
```

```
aws s3 cp ny-listings.csv s3://dataeng-landing-zone-INITIALS/listings/city=new_york_city/ny-listings.csv
```

#### IAM Roles for Redshift

- AWS Management Console - IAM Roles: https://console.aws.amazon.com/iamv2/home?#/roles

#### Creating a Redshift cluster

- AWS Management Console - Redshift: https://console.aws.amazon.com/redshiftv2/

#### Creating eternal tables for querying data in S3

- The following query can be run in the Redshift Query Editor to create an external schema. Make sure to specify the ARN for the new role you created in place of the ***iam_role*** listed below.

```
create external schema spectrum_schema
from data catalog
database 'accommodation'
iam_role 'arn:aws:iam::1234567890:role/AmazonRedshiftSpectrumRole'
create external database if not exists;
```

- The following query can be run to create a new external table. Make sure to replace ***INITIALS*** in the query below with the correct identifier for your Landing Zone bucket.

```
CREATE EXTERNAL TABLE spectrum_schema.listings(
  listing_id INTEGER,
  name VARCHAR(100),
  host_id INT,
  host_name VARCHAR(100),
  neighbourhood_group VARCHAR(100),
  neighbourhood VARCHAR(100),
  latitude Decimal(8,6),
  longitudes Decimal(9,6),
  room_type VARCHAR(100),
  price SMALLINT,
  minimum_nights SMALLINT,
  number_of_reviews SMALLINT,
  last_review DATE,
  reviews_per_month NUMERIC(8,2),
  calculated_host_listings_count SMALLINT,
  availability_365 SMALLINT)
partitioned by(city varchar(100))
row format delimited
fields terminated by ','
stored as textfile
location 's3://dataeng-landing-zone-INITIALS/listings/';
```

- The following two queries create partitions for our Jersey City and New York City data. *Make sure to run each of these queries separately, and to replace **INITIALS** with the correct identifier for your Landing Zone bucket.*

**Query 1:**  
```
alter table spectrum_schema.listings add
partition(city='jersey_city')
location 's3://dataeng-landing-zone-INITIALS/listings/city=jersey_city/'
```
**Query 2:**  
```
alter table spectrum_schema.listings add
partition(city='new_york_city')
location 's3://dataeng-landing-zone-INITIALS/listings/city=new_york_city/'
```

- Validate that the data has been loaded and defined correctly by running queries using both Redshift and Amazon Athena.

**Redshift Query:**  
```
select * from spectrum_schema.listings limit 100;
```

**Amazon Athena Query:**  
```
select * from accommodation.listings limit 100;
```

#### Creating a schema for a local Redshift table

- Create new local (not external) Redshift schema

```
create schema if not exists accommodation_local;
```

- Create new local listings table

```
CREATE TABLE dev.accommodation_local.listings(
  listing_id INTEGER,
  name VARCHAR(100),
  neighbourhood_group VARCHAR(100),
  neighbourhood VARCHAR(100),
  latitude Decimal(8,6),
  longitudes Decimal(9,6),
  room_type VARCHAR(100),
  price SMALLINT,
  minimum_nights SMALLINT,
  city VARCHAR(40))
distkey(listing_id)
sortkey(price);
```

- Load data from our Redshift Spectrum (external) table into the new local table

```
INSERT into accommodation_local.listings
(SELECT listing_id,
  name,
  neighbourhood_group,
  neighbourhood,
  latitude,
  longitudes,
  room_type,
  price,
  minimum_nights
FROM spectrum_schema.listings);
```

#### Running complex SQL queries against our data
In this section we create a complex query, but do so in steps in order to better understand how the query works.

**Query 1**
```
WITH touristspots_raw(name,lon,lat) AS (
  (SELECT 'Freedom Tower', -74.013382,40.712742) UNION
  (SELECT 'Empire State Building', -73.985428, 40.748817)),
  touristspots (name,location) AS (SELECT name,
  ST_Point(lon, lat) FROM touristspots_raw)
select name, location from touristspots
```

**Query 2**
```
WITH accommodation(listing_id, name, room_type, location) AS (SELECT listing_id, name, room_type, ST_Point(longitudes, latitude) from accommodation_local.listings)
select listing_id, name, room_type, location from accommodation
```

**Query 3**
```
WITH touristspots_raw(name,lon,lat) AS (
  (SELECT 'Freedom Tower', -74.013382,40.712742) UNION
  (SELECT 'Empire State Building', -73.985428, 40.748817)
),
touristspots(name,location) AS (
  SELECT name, ST_Point(lon, lat)
  FROM touristspots_raw),
accommodation(listing_id, name, room_type, price,
location) AS
(
  SELECT listing_id, name, room_type, price,
  ST_Point(longitudes, latitude)
  FROM accommodation_local.listings)
SELECT
  touristspots.name as tourist_spot,
  accommodation.listing_id as listing_id,
  accommodation.name as location_name,
  (ST_DistanceSphere(touristspots.location,
  accommodation.location) / 1000)::decimal(10,2) AS
  distance_in_km,
  accommodation.price AS price,
  accommodation.room_type as room_type
  FROM touristspots, accommodation
WHERE tourist_spot like 'Empire%'
ORDER BY distance_in_km
LIMIT 100;
```

**Query 4**
```
CREATE MATERIALIZED VIEW listings_touristspot_distance_view AS
WITH touristspots_raw(name, lon, lat) AS (
    (SELECT 'Freedom Tower', -74.013382,40.712742) UNION
    (SELECT 'Empire State Building', -73.985428, 40.748817)
),
touristspots(name,location) AS (
  SELECT name, ST_Point(lon, lat)
  FROM touristspots_raw),
accommodation(listing_id, name, room_type, price,location) AS
(
  SELECT listing_id, name, room_type, price, ST_Point(longitudes, latitude)
  FROM accommodation_local.listings)
SELECT
    touristspots.name as tourist_spot,
    accommodation.listing_id as listing_id,
    accommodation.name as location_name,
    (ST_DistanceSphere(touristspots.location,accommodation.location) / 1000)::decimal(10,2) AS distance_in_km,
    accommodation.price AS price,
    accommodation.room_type as room_type
FROM touristspots, accommodation
```

**Query 5**
```
select * from listings_touristspot_distance_view
where tourist_spot like 'Empire%' 
order by distance_in_km
limit 100
```



