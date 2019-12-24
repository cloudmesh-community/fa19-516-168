# Mutiple source cloud based datawarehouse

Deepak Deopura fa19-516-168

:o2: progress unclear

:o2: use proper spaces after ,

Gregor thought originally 2 differnt databases are on the data sources 
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
storing images from aws into our cloudmesh mongodb

## Abstract

* AWS to/from Azure data transfer using APIs.
* Extended version can be push data in SQL base warehouse (for example
  snowflake warehouse. It may be out of scope for now for this project
  purpose.

## New Abstract
* Connect ot Azure synapse data warehouse and use cm commands to interact with it
* Azure sysapse scale-up/scale-out using command
* Read /write data in Azure synapse database using files

## Objective

Develop APIs to transfer file data from AWS and Azure to cloud hosted
database in AWS(MariaDB).

## New Objective
Develop APIs to interact with Google Bigquery data warehouse 

## Motivation

come up with a real motivation not just replication of snowflake

use NIST OpenAPI specification for formulation abstract data ware
housing services

* Learn about various data warehouse solution provided by major cloud 
  provide (AWS,Azure,Google)
* Learn to work with cloud base datawarehouse and interaction with 
  datawarehouse from cloud or local machine
* Learn about Open APIs
* Understand data flow from/to datawarehouse, cloud and local

showcase on an application


## Terminology

what is data warehouse? 

Data warehouse is used to collect data from multiple source system
including RDBMS, transaction system, files and  and process data for
analytical and decision support system. datawarehose is used for
business reporting, historical data analysis, dashboarding for better
decision support.

what is different to rdbs ?
RDBMS is relational database to support and record transaction.

what is difference to ???

Data warehouse purpose is to support analytics and reporting and does
not need real time data. It is optimized for data querying. data is
collected from multiple sources and processed to have single point of
truth of data. Data model is mostly denormalized to have efficient query
time. Transaction database purpose is to to record data transaction and
it is optimized for insert/update then querying data. data model is
highly normalized and data processing is real time.

what is NIST BDRA and how does it fit in this project

## Releated Technologies

Snowflake:

Motivation of this project is from *Snowflake cloud warehouse*
(<https://www.snowflake.com>) . I am using snowflake cloud base warehouse
form some of my clients. Snowflake is currently providing most of their
services in AWS. They are also increasing their footprint in Azure and
will soon start on Google cloud. I would like to use this project
opportunities when there are multiple clouds in an organization and they
want to build warehouse based on various data sources across clouds.

There are likely others

* what is aws doing or not? AWS data warehouse solution is AWS Redshift

* what is azure doing or not? Azure Synapse Analytics isn sql base data
* warehouse and analytics solution by Azure

* what is google doing? BigQuery by Goolge cloud solution for data
* warehouse

how does streaming contrast this effort?

## Architecture

Definition of an OPenAPI for datawarehousing Programmatically control
warehouse clusters, scale up and scale out of machines and perform
database administration, DDL and DML commands. Limitations

Are there existing efforts?

TBD

## Cloudbased datawareouse solution comparison

Datawarehouse solution can be compared based on some of following parameters
* Ability to scale up or scale out without affecting data. So that 
  datawarehouse can be scale up for high load data job or scale out 
  to support concurrent jobs
* Independent of storage and compute
* Type of supported data like structural, JSON, semi structured, unstructured
* SQL and other support for easiness to query data


## Technology

* AWS
* Azure
* Python
* Cloudmesh storage and databse
* NIST Cloudmesh Database abstraction (done by other student of this 
  class Harsha, look up report)
* NIST REST API


### OpenAPI

TBD link to spec

### Server API

* specify the operationID's
* specify how to run
* implement for 2 database technologies as it otherwise does not make sense

* as students have likely figured out how to start databases on various
  cloud you also have to show how to host the database on the cloud
  (this last step may prevent you from completing in time, as it
  requires some experimenting on your part, but as you said you have
  experience, this should not be an issue.
  

### Manual

Describe how to run while making as much as possible automated
e.g. cms sys command generate ... (excersie from class)

    
        Usage:
        googlebigquery create [DATASET_ID] [PROJECT_ID]
        googlebigquery list [PROJECT_ID]
        googlebigquery delete [DATASET_ID] [PROJECT_ID]
        googlebigquery listtables PROJECT_ID DATASET_ID
        googlebigquery loadtable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        googlebigquery exporttable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
        googlebigquery runquery PROJECT_ID DATASET_ID [TABLE_ID] [QUERY_TXT]
        googlebigquery listjob [PROJECT_ID]


        Arguments:
            DATASET_ID              The Google bigquery dataset id.
            PROJECT_ID              The google big query project id
            TABLE_NAME              The name of the table
            JOB_ID                  The job id in bigquery
            SOURCE                  Local file which need to be load into bigquery table

        Description:
            googlebigquery create [DATASET_ID] [PROJECT_ID]
                Create a dataset in given project

            googlebigquery list [PROJECT_ID]
                List all datasets present in given project_id

            googlebigquery delete [DATASET_ID] [PROJECT_ID]
                Delete dataset from given project

            googlebigquery listtables PROJECT_ID DATASET_ID
                List all tables from given dataset and project

            googlebigquery loadtable SOURCE PROJECT_ID DATASET_ID [TABLE_ID]
                Lod source file into given table

            googlebigquery runquery PROJECT_ID DATASET_ID [TABLE_ID] [QUERY_TXT]
                run given QUERY_TXT
            
            googlebigquery listjob [PROJECT_ID]
            List all jobs present in given project_id

## Testing

develop pytests that automate testing you prg and service work, 
best done with kubernetes as you do have windows.

do benchmarks also with various size of data

so you need lots of tests and some minor benchmarks

## benchmarks

variable: cloudmesh storage providers: local, azure, aws, google (box)
variable: data size: figure out what impact datasize has
??? variable: where to place the datawarese: local ???, aws warehose???, aws maridb???
????

use case: is there a usecase that we can use that is not from your company? 
Maybe something we can simulate, with files. 

Some of use cases of cloud based data warehouse
* Use cloud scale up to run heavy data load job 
* Use scale out to support multiple queries from user for better performance
* Able to programmatically control data warehouse based on job size and load on system

Evaluate what this does:

* <https://github.com/cloudmesh/cloudmesh-redshift> (what is this,)

This package is used to interact with AWS redshift data warehouse. It is
used to externally interact with redshif cluster, increase size of
cluster, rename cluster, change password etc. It also allow used to do
basic DDL and DML operation on database hosted on redshift. I think
objective of my project can be slightly changed to interact with Azure
data warehouse. We have implementation in cloudmesh for storage,
compute, database. We can similarly have implementation for all
datawarehouse services provided by different cloud provide. As redshift
is already implementated so my project can be focused to include Azure
data warehouse in cloudmesh bundle. We can build cloudmesh package for
datawarehose from various cloude provide ( similar to cloudmesh-storage,
cloudmesh-compute etc)

## Progress

* Installed cloudmesh on Windows 10
* Created cloud account on AWS, AZURE and Google
* Compared various data warehouse solution provided by major clod 
  provider (AWS redshift,Azure-Synapse,Google-BigQuery)
* Created sample data base on BigQuery,Azure Synapse and AWS red shift
* Checked for Python libraries require to connect to BigQuery, Redshift 
  and Azure warehouses
* Created functions to run queries from python

## Reference

* <https://docs.microsoft.com/en-us/azure/sql-data-warehouse/>
* <https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html>
* <https://cloud.google.com/bigquery/docs/>
