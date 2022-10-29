import csv
import mysql.connector as connection
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('USE FSDS')

#cursor.execute("CREATE PROCEDURE GetAllRows3(IN var INT) BEGIN select * from bank_marketing LIMIT var; END")

cursor.execute("call GetAllRows3(2)")
print(cursor.fetchall())
