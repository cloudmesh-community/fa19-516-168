from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('C:\Deepak\MS\BQ\cmddeopura-019c0c55e161.json')
project_id = 'cmddeopura'
client = bigquery.Client(credentials= credentials,project=project_id)

def samlequery():
    query_txt="SELECT CONCAT( 'https://stackoverflow.com/questions/',       CAST(id as STRING)) as url,  view_count FROM `bigquery-public-data.stackoverflow.posts_questions` WHERE tags like '%google-bigquery%' ORDER BY view_count DESC LIMIT 10"
    query_job = client.query(query_txt)
    results = query_job.result()
    for row in results:
        print("{} : {} views".format(row.url, row.view_count))

def listdatasets():
    datasets = list(client.list_datasets())

    project = client.project
    if datasets:
        print("Datasets in project {}:".format(project))
        for dataset in datasets:
            print("\t{}".format(dataset.dataset_id))
    else:
        print("{} project does not contain any datasets.".format(project))

def createdataset():
    print("creating dataset")

def loaddata():
    print("Loading data")
    #client = bigquery.Client()
    filename = '/empsample.csv'
    dataset_id = 'cmddeopura:emp_table'
    table_id = 'cmddeopura:emp_table.employee_table'

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Waits for table load to complete.

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))

#listdatasets()
#samlequery()

loaddata()