"""d"""
import mysql.connector

cnx = mysql.connector.connect(user='root', password='Porsche*911',
                              host='127.0.0.1',
                              database='firstmysql')
print(cnx._execute_query('SHOW DATABASES'))
cnx.close()
