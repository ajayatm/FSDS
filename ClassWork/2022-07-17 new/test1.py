import datetime
import mysql.connector as connection
import csv
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('CREATE DATABASE IF NOT EXISTS INEURON')
cursor.execute('USE FSDS')
cursor.execute("CREATE TABLE IF NOT EXISTS SANDP500 (Date DATE, Close FLOAT, Open FLOAT, High FLOAT, Low FLOAT)")
#cursor.execute('DESCRIBE SANDP500')
#print(cursor.fetchall())
#with open('S&P 500.csv', newline='') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=',')
    #for row in spamreader:
        #x = datetime.datetime.strptime(row[0], "%m/%d/%Y").strftime('%Y-%m-%d')
        #print(x)
        #cursor.execute("INSERT INTO SANDP500 values(%s,%s,%s,%s,%s)", [x,float(row[1]),float(row[2]),float(row[3]),float(row[4])])
#mydb.commit()
cursor.execute("SELECT count(*) from SANDP500 where Close < 3000")
for i in cursor.fetchall():
    print(i)

cursor.execute("SELECT count(*), YEAR(Date) from SANDP500 group by 2")
for i in cursor.fetchall():
    print(i)