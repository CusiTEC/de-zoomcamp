# Week 4: Analytics Engineering 


### Prerequisites
By this stage of the course you should have already: 

- A running warehouse (BigQuery) 
- A set of running pipelines ingesting the project dataset (week 3 completed)
- The following datasets ingested from the course :
  * Yellow taxi data - Years 2019 and 2020
  * Green taxi data - Years 2019 and 2020 
  * fhv data - Year 2019. 

NOTE : For this part, use Mage to load the data into parquet and from there create a table in BigQuery, you can see the code in the attached `.py` files.

## Questions
Question 1. Dbt build 

`It applies a limit 100 only to our staging models`
```
-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
```

Question 2. Code for the CI job 

`The code from a development branch requesting a merge to main`

Question 3. Count of records in fhv trips 

These dbt commands are building specific models (stg_green_tripdata, stg_yellow_tripdata, stg_fhv_tripdata) and also all available models without specific restriction. The is_test_run variable is set to false, which could indicate that this run is not a test run. Building models in dbt typically involves running SQL queries defined in model files and creating or updating tables in the database based on those queries.
```
dbt build --select stg_green_tripdata --vars '{'is_test_run':'false'}'
dbt build --select stg_yellow_tripdata --vars '{'is_test_run':'false'}'
dbt build --select stg_fhv_tripdata --vars '{'is_test_run':'false'}'
dbt build --vars '{'is_test_run':'false'}'
```
Question 4. Service with the most rides 

`Yellow`