
# Week 3 Homework

For this homework we will be using the 2022 Green Taxi Trip Record Parquet Files from the New York City Taxi Data found here:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page


NOTE: DATA INGESTED INTO BIGQUERY WITH MAGE

### Question 1: 
What is count of records for the 2022 Green Taxi Data??

ANSWER:
```
SELECT count(*) FROM `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022`;
```

### Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

ANSWER:
```
SELECT COUNT(DISTINCT(PULocationID)) 
FROM `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022`;

SELECT COUNT(DISTINCT(PULocationID)) 
FROM `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022_no_partitioned`;
```

### Question 3:
How many records have a fare_amount of 0?

ANSWER:
```
SELECT COUNT(*) FROM `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022` 
WHERE fare_amount = 0;
```

### Question 4:
What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)


ANSWER:
```
CREATE OR REPLACE TABLE `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS (
SELECT * FROM `zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022`);
```
### Question 5:
Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime
06/01/2022 and 06/30/2022

ANSWER:
```
SELECT DISTINCT PULocationID FROM  
`zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022_no_partitioned` 
WHERE DATE(lpep_pickup_datetime) 
BETWEEN '2022-06-01' AND '2022-06-30'

SELECT DISTINCT PULocationID FROM  
`zoomcamp-dataengineer.ny_green_taxi.green_taxi_2022_partitioned`
WHERE DATE(lpep_pickup_datetime) 
BETWEEN '2022-06-01' AND '2022-06-30'
```
### Question 6: 
Where is the data stored in the External Table you created?

ANSWER:
```
GCP Bucket
```

### Question 7:
It is best practice in Big Query to always cluster your data:

ANSWER:
```
True
```