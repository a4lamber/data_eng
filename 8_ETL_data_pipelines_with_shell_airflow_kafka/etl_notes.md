# ETL and ELT Processes

> ETL is a acronym for an automated data pipeline engineering methodology.

## What's ETL

Extraction, transform and load (ETL)  is an automated datapipeline engineering methodology illustrated as 

```mermaid
flowchart LR
    Extract --> Transform
    Transform --> Load
```



- extraction:
  
  - Description: configurng access to data and reading it into an application
  
  - Sources: Various API, web scrapping

- transformation
  - Descrption: processing data to make it conform to the requirements of both the target system or intended database
  - Sources: 
    - Processing data
    - Conforming to target system or use cases
    - Cleaning
    - Filtering
    - Joining
    - Feature engineering (?)
    - Formatting and data typing (casting etc)
- load
  - Description: loading data into a new environment such as a database, data warehouse or data mart.
  - Making the data readily available for analytics, dashboards, reports.



**Use cases for ETL pipelines**

- digitizing analog media
- moving data from OLTP systems to OLAP system
- dashboards for sales, marketing



**summary**

- ETL stands for Extract, transform and load

- Extraction means reading data from one or more sources

- Transformation means wrangling data to meet destination requirements

- loading means writing the data to its destination environment

- ETL is used for curating data and making it accessible to end users.

## What's ELT

>  Outline:
> 
> - what it ELT
> - why ELT is an emerging trend?



Cases of ELT:

- d
- d

As for why ELT is an emerging trend:

- ELT separates the data pipeline from the processing
- No information loss
- Cuz cloud platforms are enabling it

## Comparing ETL to ELT

Outline:

- difference between ETL and ELT

Summary:

- incresing demand for access to raw data drives the evolution from ETL to ELT

## Data Extraction Technuqies

Outline

- list examples of raw data sources
- s
- s

examples of raw data sources are:

- paper documents
- web pages
- analog audio/video
- survey, statistics and economics
- transcational data

Techniques for extracting data:

- OCR
- ADC sampling
- CCD sampling
- Mail, phone or in-person
- Web scraping
- APIs 
- database querying
- Edge computing
- biomedical devices that extracting data series

## Intro to data trans techniques

Outline:

- name data transformation techniques
- compare `schema-on-write` vs `schema-on-read`
- list ways info can be lost in transformation

> formatting the data to suit the application

- data typing (casting to apporiate)
- data structuring (json, csv,xml to db table)
- Anonymizing, encrypting
- Cleaning
  - duplicate records, missing values
- normalizing
  - converting data to common units
- filtering
  - sorting, aggregating, binning
- joining data sources

information loss in transformation

- lossy data compression
- filtering
- aggregation
- edge computing devices

Summary:

- ELT for schema-on-read while ETL for schema-on-write

## data loading transformation

outline:

- list data loading techniques
- differentiate batch loading from stream loading
- explain push vs pull
- describe parallel loading

full loading vs incremental loading

scheduled vs on-demand loading

batch vs stream loading vs mini-batch loading

Client-server model

- pull: requests for data originate from the client
- for 
- push:
- for 

# ETL with shell

---

## ETL using shell scripts

Step 1: Create an ETL shell script

```bash
touch Temperature_ETL.sh
gedit Temperature_ETL.sh
#! /bin/bash
# Extract reading with get_temp_API
# Append reading to temperature.log
# Buffer last hour of readings
# Call get_stats.py to aggregate the readings
# Load the stats using load_stats_api
```

Step 2: Schedule it to run every minute

```bash
touch temperature.log
#! /bin/bash
# Extract reading with get_temp_API
# Append reading to temperature.log
get_temp_api >> temperature.log

# Buffer last hour of reading

tail -60 temperature > temperature.log
```

Step 3: ETL scripts transform temperature

`get_stats.py`

- reads temperatures from log file

- calculates temperature stats

- Writes temperature stats to file

- Input/output filenames specified as command line arguments
  
  ```bash
  # Call get_stats.py to aggregate the readings
  ```

python3 get_stats.py temperature.log temp_stats.csv

```bash
Step 4:Load the transformation
```

load the stats using load_stats_api

load_stats_api temp_stats.csv

```bash
Step 5: Schedule ur ETL job
- open crontab `crontab -e`
- enter schedule `1 * * * path/Temperature_ETL.sh`
- close and save
- ur job is now scheduled and running in production

> Summary: You have learnt
> - ETL pipelines can be created with Bash scripts
> - ETL jobs can be run on a schedule using `cron`
```

# Introduction to data pipelines

---

## Brief intro to data pipeline

Outline:

- define pipeline performance with `letency` and `throughout`

- talk about some use cases





Use cases:

- bakcing up files

- streaming data from IoT devices to dashboards



Summary:

In this video, you learned that

- data pipelines move data from one place or form to another

- data flows through pipelines as a series of data packets

- latency and throughput are key design considerations for data pipelines

- data pipelines use cases range from simple copy-and-paste to online video meetings





## Key data pipeline process

Outline:

- last key data pipeline processes

- describe data pipeline monitoring considerations

- describe data pipeline solutions for mitigating data flow bottlenecks



Summary:

- data pipeline processes include scheduling or triggering, monitoring, maintenance and optimization

- pipeline monitoring - tracking latency, throughput, resource utilization, and failures

- parallelization and I/O buffers can help mitigate bottlenecks




