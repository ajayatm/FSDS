import csv
import mysql.connector as conn
import pandas as pd
import os


class Connection:

    mydb = conn.connect(host='localhost', user='root', password='Porsche*911')
    data = pd.read_sql('select * from firstmysql.glassdata', mydb)
    print(data)
    databases = pd.read_sql('show databases', mydb)
    print(databases)
