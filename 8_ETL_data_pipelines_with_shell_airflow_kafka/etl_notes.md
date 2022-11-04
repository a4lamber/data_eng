# ETL and ELT Processes

> ETL is a acronym for an automated data pipeline engineering methodology.

## What's ETL

ETL:
- exraction
  - Sources: API, web scrapping
- transformation
- loading
  - Defintion:



Application cases for ETL pipelines:
- digitizing analog media
- moving data from OLTP systems
- dashboards




## What's ELT

Outline:
- what it ELT
- why ELT is an emerging trend?


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
  -  duplicate records, missing values
-  normalizing
   -  converting data to common units
-  filtering
   -  sorting, aggregating, binning
-  joining data sources


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

```
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
```
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
```
# Call get_stats.py to aggregate the readings

python3 get_stats.py temperature.log temp_stats.csv
```

Step 4:Load the transformation
```
# load the stats using load_stats_api
load_stats_api temp_stats.csv
```


Step 5: Schedule ur ETL job
- open crontab `crontab -e`
- enter schedule `1 * * * path/Temperature_ETL.sh`
- close and save
- ur job is now scheduled and running in production

> Summary: You have learnt
> - ETL pipelines can be created with Bash scripts
> - ETL jobs can be run on a schedule using `cron`

