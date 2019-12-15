import mysql.connector as mariadb
import csv

mariadb_connection = mariadb.connect(host='database-2.ch4ii9cu38zh.us-east-2.rds.amazonaws.com',port='3306',user='admin', password='Ohio*1234', database='testcm')
cursor = mariadb_connection.cursor()
cursor.execute("SELECT id,name FROM test_student")
#print(cursor[0])
for id, name in cursor:
    print(id,name)
f=open('C:\\Users\\ddeopura\\cm\\student.csv')
csv_data = csv.reader(f)
#for row in csv_data:
#    print(row[0])

for row in csv_data:
    #print(row[0])
    cursor.execute('INSERT INTO test_student (id, name) VALUES (%s, "%s")', row)
#close the connection to the database.
mariadb_connection.commit()
cursor.close()
print("complted")
