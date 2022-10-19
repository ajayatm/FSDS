import mysql.connector as connection

mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
#cursor.execute('CREATE DATABASE FSDS')
#cursor.execute('SHOW DATABASES')
#cursor.execute('CREATE TABLE IF NOT EXISTS FSDS.SUBJECTS(NAME VARCHAR(50), CLASSES INT(3), ASSIGNMENTS INT(3), PROJECTS INT(3))')
cursor.execute('SHOW DATABASES')
#cursor.execute("INSERT INTO FSDS.SUBJECTS VALUES('STATISTICS',5,10,10)")
cursor.execute('SELECT * FROM FSDS.SUBJECTS')
cursor.execute('SHOW DATABASES')
print(cursor.fetchall())
mydb.commit()
