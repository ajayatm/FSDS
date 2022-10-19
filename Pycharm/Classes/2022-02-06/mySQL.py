import mysql.connector as conn
import pandas as pd
import csv


class MySQL:
    mydb = conn.connect(host='localhost', user='root', password='Porsche*911')
    cursor = mydb.cursor()

    cursor.execute('USE firstmysql')
    cursor.execute('SELECT * from car_evaluation WHERE doors = "4"')
    print(cursor.fetchall())
