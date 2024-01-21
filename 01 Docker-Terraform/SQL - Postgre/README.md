
# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)

# Note
In the jupter notebook file pg-test-connection.ipynb you will find the python code from the ETL to postgres and the SQL used for the answers to the questions. In my case

In this README.md I will place the Sql code used.

## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

### Answer
```
SELECT COUNT(*) AS total_trips
FROM green_tripdata_trip
WHERE lpep_pickup_datetime >= '2019-09-18' AND lpep_pickup_datetime < '2019-09-19'
AND lpep_dropoff_datetime >= '2019-09-18' AND lpep_dropoff_datetime < '2019-09-19';
```

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### Answer
```
SELECT
  date(lpep_pickup_datetime),
  MAX(trip_distance) as max_trip_distance
FROM green_tripdata_trip
GROUP BY date(lpep_pickup_datetime)
ORDER BY max_trip_distance DESC;
```

## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"


### Answer
```
SELECT
  z."Borough",
  SUM(t."total_amount")
FROM green_tripdata_trip t 
INNER JOIN zones z
ON t."PULocationID" = z."LocationID"
WHERE date(lpep_pickup_datetime) = '2019-09-18'
AND z."Borough" <> 'Unknown'
GROUP BY z."Borough"
HAVING SUM(t."total_amount") >=50000;
```

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza


### Answer
```
SELECT
  z2."Zone",
  MAX(t."tip_amount") AS max_tip
FROM green_tripdata_trip t
INNER JOIN zones z
ON t."PULocationID" = z."LocationID"
INNER JOIN zones z2
ON t."DOLocationID" = z2."LocationID"
WHERE date(t."lpep_pickup_datetime") BETWEEN '2019-09-01' AND '2019-09-30'
AND z."Zone" = 'Astoria'
GROUP BY z2."Zone"
ORDER BY max_tip DESC
LIMIT 1;
```