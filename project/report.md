# Mutiple source cloud based datawarehouse

Deepak Deopura fa19-516-168


Gregor thought originally 2 differnt databases are on the data sources 
but that may not be the case ??? as clarification was done by student 
he does only file based data sources.

student will correct this in writeup. remember students form class have
implemented various things in different clouds that can be leveraged,
you willl have to develop likely one that is not yet done plus what you
do in this project. you can start with what students have implemented,
look at awss3 provider, google, azure are forthcomming, local was notyet
don, which you should use ;-) as this would allow you to simulate the
dataware house locally as well as the db, thus speeding up your
development due to limited time


:o2: please learn markdown

:o2: this project has significant issues as tehchnology such as
snowflake is use that does not provide a free tier. The 30 day free
licensis is insufficient. Please chose a different technology for
testing. However you can in addition to some other artifact certaily use
snowflake, but it can ot be your main objective. When reading your
comment you actually do understand the issue .... Maybe you can use
MariaDB or something like that. Also remember you need to technically
compare streaming vs backu and upload. What we found n AWS is that
streaming for data takes 45 min while backing up and reload 2 minutes
.... however we have not spend any time optimiszing this. This is
storing images from aws into our cloudmesh mongodb

## Abstract

- AWS to/from Azure data transfer using APIs.
- Extended version can be push data in SQL base warehouse (for example
  snowflake warehouse. It may be out of scope for now for this project
  purpose.

## Objective

Develop APIs to transfer file data from AWS and Azure to cloud hosted database in AWS(MariaDB).



## Motivation

come up with a real motivation not just replication of snowflake

use NIST OpenAPI specification for formulation abstract data ware housing services 

- Learn about cloud base database warehouse and interaction with database from cloud or local machine
- Learn about Open APIs
- Understand data flow from/to cloud and database 
showcase on an application


## Ternminology

what is data warehouse? 
Data warehouse is used to collect data from multiple source system including RDBMS, transaction system, files and  and process data for analytical and decision support system.
datawarehose is used for business reporting, historical data analysis, dashboarding for better decision support. 

what is different to rdbs ?
RDBMS is relational database to support and record transaction.

what is difference to ???
Data warehouse purpose is to support analytics and reporting and does not need real time data. It is optimized for data querying.
data is collected from multiple sources and processed to have single point of truth of data.
Data model is mostly denormalized to have efficient query time.
Transaction database purpose is to to record data transaction and it is optimized for insert/update then querying data.
data model is highly normalized and data processing is real time. 


what is NIST BDRA and how does it fit in this project

## Releated Technologies

Snowflake:

Motivation of this project is from *Snowflake cloud warehouse*
(https://www.snowflake.com) . I am using snowflake cloud base warehouse
form some of my clients. Snowflake is currently providing most of their
services in AWS. They are also increasing their footprint in Azure and
will soon start on Google cloud. I would like to use this project
opportunities when there are multiple clouds in an organization and they
want to build warehouse based on various data sources across clouds.

There are likely others

- what is aws doing or not? - AWS data warehosue solution is AWS Redshift
- what is azure doing or not - Azure Synapse Analytics
- what is google doing - BigQuery by Goolge cloud

how daes streaming contrast this effort?

## Architecture

Definition of an OPenAPI for datawarehousing

Limitations

Are ther existing efforts?

TBD

## Technology

* AWS
* Azure
* Python
* Cloudmesh storage
* NIST Cloudmesh Database abstraction (done by other student of this class Harsha, look up report)
* NIST REST API

### OPenAPI

TBD link to spec

### Server API

* specify the operationID's
* specify how to run
* implement for 2 database technologies as it otherwise does not make sense
* as students have likely figured out how to start databases on various cloud 
  you ols have to show hwo to host the database on the cloud (this last step 
  may prevent you from completing in time, as it requires some experimenting 
  on your part, but as you said you have experience, this should not be 
  an issue.
  

### Manual

Describe how to run while making as much as possibe automated
e.g. cms sys command generate ... (excersie from class)

## Testing

develop pytests that automate testing you prg and service work, 
best done with kubernetes as you do have windows.

do benchmarks also with various size of data

so you need lots of tests and smom minor benchmarks

## benchmarks

variable: cloudmesh storage providers: local, azure, aws, google (box)
variable: data size: figure out what impact datasize has

??? variable: where to place the datawarese: local ???, aws warehose???, aws maridb???
????

use case: is there a usecase that we can use that is not from your company? 
Maybe something we can simulate, with files. 

Evaluate what this does:

* https://github.com/cloudmesh/cloudmesh-redshift (what is this,)

