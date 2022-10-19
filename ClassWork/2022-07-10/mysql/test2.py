import mysql.connector as connection

mydb = connection.connect(host='localhost', user='root',password='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('SELECT NAME, ASSIGNMENTS FROM FSDS.SUBJECTS')
print(cursor.fetchall())
