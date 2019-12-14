from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('C:\Deepak\MS\BQ\cmddeopura-019c0c55e161.json')
project_id = 'cmddeopura'
client = bigquery.Client(credentials= credentials,project=project_id)

query_txt="SELECT CONCAT( 'https://stackoverflow.com/questions/',       CAST(id as STRING)) as url,  view_count FROM `bigquery-public-data.stackoverflow.posts_questions` WHERE tags like '%google-bigquery%' ORDER BY view_count DESC LIMIT 10"
query_job = client.query(query_txt)
results = query_job.result()
for row in results:
    print("{} : {} views".format(row.url, row.view_count))