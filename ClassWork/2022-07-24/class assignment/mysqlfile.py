from sqlalchemy import create_engine
import mysql.connector as connection
import pandas as pd
import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")

engine = create_engine("mysql+pymysql://" + "root" + ":" + "Porsche*911" + "@" + "localhost" + ":" + "3306" + "/" + "FSDS" + "?" + "charset=utf8mb4")
conn = engine.connect()
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('USE FSDS')

def loadingtables(input1, input2):
    excel_file = pd.ExcelFile(input1)
    excel_dataframe = excel_file.parse(sheet_name="Sheet1")
    excel_dataframe.to_sql("attribute_data", conn, if_exists="replace")
    excel_file = pd.ExcelFile(input2)
    excel_dataframe = excel_file.parse(sheet_name="Sheet1")
    excel_dataframe.to_sql("dress_sales", conn, if_exists="replace")

def leftjoin():
    cursor.execute('SELECT * FROM attribute_data left join dress_sales on attribute_data.dress_id = dress_sales.dress_id')

def noofdress():
    cursor.execute('SELECT COUNT(*) FROM DRESS_SALES')
    print(cursor.fetchone())
    cursor.execute('SELECT COUNT(distinct dress_id) FROM DRESS_SALES')
    print(cursor.fetchone())
    cursor.execute('SELECT COUNT(*) FROM attribute_data')
    print(cursor.fetchone())
    cursor.execute('SELECT COUNT(distinct dress_id) FROM attribute_data')
    print(cursor.fetchone())

def zerorecommendation():
    cursor.execute('select count(*) from attribute_data where recommendation = 0')
    print(cursor.fetchone())
    cursor.execute('select count(distinct dress_id) from attribute_data where recommendation = 0')
    print(cursor.fetchone())
    cursor.execute('select * from attribute_data where dress_id in (select dress_id from attribute_data group by dress_id having count(recommendation) > 1) order by dress_id')
    cursor.execute('select a.dress_id from attribute_data a inner join attribute_data b on a.dress_id = b.dress_id and a.recommendation = 0 and b.recommendation = 1 order by a.dress_id')

def totalsales():
    cursor.execute("select dress_id, (A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W) from dress_sales order by dress_id")

def thirdhighest():
    cursor.execute("select dress_id, A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W from dress_sales order by 2 desc limit 2,1")

def pandasdf():
    df1 = pd.read_excel('D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Attribute DataSet.xlsx')
    df2 = pd.read_excel('D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Dress Sales.xlsx')
    df1.to_json('D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Attribute DataSetJSON.json')
    df2.to_json('D:\\Ajay\\Education\\iNeuron\\FSDS\\ClassWork\\2022-07-24\\class assignment\\Dress Sales JSON.json')
    database = client['mongotest']
    collection = database["attribute_data"]
    collection.insert_many(df1.to_dict(orient='records'))
    collection = database["dress_sales"]
    collection.insert_many(df2.to_dict(orient='records'))
