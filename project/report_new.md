# Cloudmesh Google BigQuery 

* Deepak Deopura, fa19-516-168
* Gregor von Laszewski

:o2: progress unclear

Gregor thought originally 2 different databases are on the data sources 
but that may not be the case ??? as clarification was done by student 
he does only file based data sources.

student will correct this in writeup. remember students form class have
implemented various things in different clouds that can be leveraged,
you will have to develop likely one that is not yet done plus what you
do in this project. you can start with what students have implemented,
look at awss3 provider, google, azure are forthcomming, local was notyet
don, which you should use ;-) as this would allow you to simulate the
data warehouse locally as well as the db, thus speeding up your
development due to limited time


:o2: please learn markdown

:o2: this project has significant issues as technology such as
snowflake is use that does not provide a free tier. The 30 day free
licensises is insufficient. Please chose a different technology for
testing. However you can in addition to some other artifact certaily use
snowflake, but it can ot be your main objective. When reading your
comment you actually do understand the issue .... Maybe you can use
MariaDB or something like that. Also remember you need to technically
compare streaming vs backu and upload. What we found n AWS is that
streaming for data takes 45 min while backing up and reload 2 minutes
.... however we have not spend any time optimiszing this. This is
storing images from aws into our Cloudmesh mongodb

## Abstract
- Connect ot Google BigQuery data warehouse and use Cloudmesh commands to interact with data sets and tables
- Create and delete objects in Google big query
- Read /write data from Google big query

## Objective
Develop Cloudmesh commands  to interact with Google BigQuery, a cloud based datawarehouse solution

## Motivation

- Learn about various data warehouse solution provided by major cloud providers (AWS,Azure,Google)
- Learn to work with cloud base datawarehouse and interaction with datawarehouse from cloud or local machine
- Learn about Open APIs
- Understand data flow from/to datawarehouse, cloud and local and programmatically interact with cloud hosted data warehouse

## Terminology

- What is data warehouse? 
Data warehouse is used to collect data from multiple source system including RDBMS, transaction system, files and  and process data for analytical and decision support system.
datawarehose is used for business reporting, historical data analysis, dashboarding for better decision support. 

- What is different to RDBMS?
RDBMS is relational database to support and record transaction.
Data warehouse purpose is to support analytics and reporting and does not need real time data. It is optimized for data querying.
data is collected from multiple sources and processed to have single point of truth of data.
Data model is mostly denormalized to have efficient query time.
Transaction database purpose is to to record data transaction and it is optimized for insert/update then querying data.
data model is highly normalized and data processing is real time. 

## Releated Technologies

Snowflake:

Motivation of this project is from *Snowflake cloud warehouse*
(https://www.snowflake.com) . Snowflake is currently providing most of their
services in AWS. They are also increasing their footprint in Azure and
will soon start on Google cloud. There may be multiple clouds in an organization and they may
want to build warehouse based on various data sources across clouds. Interaction with mutiple clouds from single point can help on those use cases.

Some of data warehouse solutions by major cloud providers

- AWS data warehouse solution is AWS Redshift
- Azure Synapse Analytics isn sql base data warehouse and analytics solution by Azure
- BigQuery by Goolge is cloud based solution for data warehouse

####Cloudbased datawareouse solution comparison
Data warehouse solution can be compared based on some of following parameters
* Ability to scale up or scale out without affecting data. So that data warehouse can be scale up for high load data job or scale out to support concurrent jobs
* Independent of storage and compute
* Type of supported data like structural, JSON, semi structured, unstructured
* SQL and other support for easiness to query data

## Architecture

Definition of an OPenAPI for datawarehousing
Programmatically control warehouse clusters, scale up and scale out of machines and perform database administration, DDL and DML commands. 
Limitations

Are there existing efforts?

TBD

## Technology

* Python 
: Python libraries are used to programmatically interact with cloud and cloud hosted data warehouse
* Google Big query
: Google big query is cloud hosted data warehouse and provide analytical capabilities    
* Cloudmesh
: Cloudmesh provide solution to interact with multiple clouds from single entry point.
* NIST REST API


### OpenAPI

TBD link to spec

### Server API

* specify the operationID's
* specify how to run
* implement for 2 database technologies as it otherwise does not make sense
* as students have likely figured out how to start databases on various cloud 
  you also have to show how to host the database on the cloud (this last step 
  may prevent you from completing in time, as it requires some experimenting 
  on your part, but as you said you have experience, this should not be 
  an issue.
  

### Manual

Google big query commands have been created using Cloudmesh and Python libraries to programmatically interact with BigQuery.
    
        Usage:
        googleBigQuery create [DATASET_ID] [PROJECT_ID]
        googleBigQuery list [PROJECT_ID]
        googleBigQuery delete [DATASET_ID] [PROJECT_ID]
        googleBigQuery listtables PROJECT_ID DATASET_ID
        googleBigQuery loadtable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        googleBigQuery exporttable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        googleBigQuery runquery PROJECT_ID DATASET_ID [TABLE_ID] [QUERY_TXT]
        googleBigQuery listjob [PROJECT_ID]


        Arguments:
            DATASET_ID              The Google BigQuery dataset id.
            PROJECT_ID              The google big query project id
            TABLE_NAME              The name of the table
            JOB_ID                  The job id in BigQuery
            SOURCE                  Local file which need to be load into BigQuery table

        Description:
            googleBigQuery create [DATASET_ID] [PROJECT_ID]
                Create a dataset in given project

            googleBigQuery list [PROJECT_ID]
                List all datasets present in given project_id

            googleBigQuery delete [DATASET_ID] [PROJECT_ID]
                Delete dataset from given project

            googleBigQuery listtables PROJECT_ID DATASET_ID
                List all tables from given dataset and project

            googleBigQuery loadtable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
                Lod source file into given table

            googleBigQuery runquery PROJECT_ID DATASET_ID [TABLE_ID] [QUERY_TXT]
                run given QUERY_TXT
            
            googleBigQuery listjob [PROJECT_ID]
            List all jobs present in given project_id

## Testing

develop pytests that automate testing you prg and service work, 
best done with kubernetes as you do have windows.

do benchmarks also with various size of data

so you need lots of tests and some minor benchmarks

## benchmarks

variable: Cloudmesh storage providers: local, azure, aws, google (box)
variable: data size: figure out what impact datasize has
??? variable: where to place the datawarese: local ???, aws warehose???, aws maridb???
????

use case: is there a usecase that we can use that is not from your company? 
Maybe something we can simulate, with files. 

Some of use cases of cloud based data warehouse
* Use cloud scale up to run heavy data load job 
* Use scale out to support multiple queries from user for better performance
* Able to programmatically control data warehouse based on job size and load on system

## Progress
- Installed Cloudmesh
- Created cloud account on AWS, AZURE and Google
- Compared various data warehouse solution provided by major clod provider (AWS- redshift,Azure-Synapse,Google-BigQuery)
- Created sample data base on BigQuery,Azure Synapse and AWS red shift
- Checked for Python libraries require to connect to BigQuery,Redshift and Azure warehouses
- Created functions to run queries from python
- Setup google BigQuery account and project on BigQuery
- Changed cloumehs.yaml file to include Google BigQuery credentials 
- Created Provider fro Google BigQuery.
- Create googleBigQuery commands to create, delte and list datasets from goog big query project
- Created commands to create tables, list tables from specific data set and describe tables
- Created command to create and load data from local to BigQuery
- Created pytest scrip file file to test google BigQuery commands from Cloudmesh.

##Reference
*https://docs.microsoft.com/en-us/azure/sql-data-warehouse/*
*https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html*
*https://cloud.google.com/BigQuery/docs/*
