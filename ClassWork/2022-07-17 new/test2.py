import csv
import mysql.connector as connection
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('USE FSDS')
cursor.execute("create table if not exists bank_marketing (age INT,job VARCHAR(15),marital VARCHAR(10),education VARCHAR(10),`default` VARCHAR(3),balance INT,housing VARCHAR(3),\
loan VARCHAR(3),contact VARCHAR(10),day INT,month VARCHAR(3),duration INT,campaign INT,pdays INT,previous INT,poutcome VARCHAR(10),y VARCHAR(3))")

#cursor.execute('describe bank_marketing')
#print(cursor.fetchall())

#with open('bank-full.csv') as csvfile:
#    filereader = csv.reader(csvfile)
#    next(filereader)
#    sql = "INSERT INTO bank_marketing values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#    todb = [tuple(line) for line in filereader]
#    cursor.executemany(sql,todb)
#    mydb.commit()

#cursor.execute('SELECT count(*) FROM BANK_MARKETING')
#print(cursor.fetchall())
#cursor.execute("SELECT * FROM BANK_MARKETING WHERE EDUCATION = 'PRIMARY' AND BALANCE < 100")
#cursor.execute("SELECT DISTINCT JOB FROM BANK_MARKETING")
#cursor.execute("SELECT DISTINCT JOB FROM BANK_MARKETING")
#cursor.execute("SELECT * FROM BANK_MARKETING WHERE BALANCE IN (SELECT MAX(BALANCE) FROM BANK_MARKETING)")
cursor.execute("SELECT COUNT(*), AVG(BALANCE), MARITAL FROM BANK_MARKETING WHERE BALANCE > 60000 GROUP BY MARITAL")
print(cursor.fetchall())
#cursor.execute("UPDATE BANK_MARKETING SET BALANCE = 0 WHERE JOB = 'UNKNOWN'")
cursor.execute("SELECT MIN(BALANCE) FROM BANK_MARKETING WHERE JOB = 'UNKNOWN'")
print(cursor.fetchall())
#cursor.execute("DELETE FROM BANK_MARKETING")
#mydb.commit()
