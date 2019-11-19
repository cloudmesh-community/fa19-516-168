# Mutiple source cloud based datawarehouse

deepak deopura fa19-516-168

:o2: please leran markdown

:o2: this project has significant issues as tehchnology such as snowflake is use that does not provide a free tier. The 30 day free licensis is insufficient. Please chose a different technology for testing. However you can in addition to some other artifact certaily use snowflake, but it can ot be your main objective. When reading your comment you actually do understand the issue .... Maybe you can use MariaDB or something like that. Also remember you need to technically compare streaming vs backu and upload. What we found n AWS is that streaming for data takes 45 min while backing up and reload 2 minutes ....
however we have not spend any time optimiszing this. This is storing images from aws into our cloudmesh mongodb

## Abstract

- AWS to/from Azure data transfer using APIs.
- Extended version can be push data in SQL base warehouse (for example snowflake warehouse. It may be out of scope for now for this project purpose.

## Objective

Develop APIs to transfer data between AWS and Azure.

## Motivation

Motivation of this project is from “Snowflake cloud warehouse” (https://www.snowflake.com) . I am using snowflake cloud base warehouse form some of my clients. Snowflake is currently providing most of their services in AWS. They are also increasing their footprint in Azure and will soon start on Google cloud.
I would like to use this project opportunities when there are multiple clouds in an organization and they want to build warehouse based on various data sources across clouds.

## Architecture

TBD

## Technology

-	AWS
-	Azure
-	Python
-	Cloudmesh storage
-	REST API

## Testing

TBD

