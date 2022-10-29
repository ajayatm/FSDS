# %%
import csvkit
import mysql.connector as connection
import pandas as pd
import pymongo
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://" + "root" + ":" + "Porsche*911" + "@" + "localhost" + ":" + "3306" + "/" + "FSDS" + "?" + "charset=utf8mb4")
conn = engine.connect()
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('USE FSDS')
database = client['mongotest']
#task 2 - Superstore_USA
# %%
#1. load this data in sql and in pandas with a relation in sql 
df_orders = pd.read_excel('Superstore_USA.xlsx',0)
df_returns = pd.read_excel('Superstore_USA.xlsx',1)
df_users = pd.read_excel('Superstore_USA.xlsx',2)
# %%
#2 . while loading this data you dont have to create a table manually you can 
# use any automated approach to create a table and load a data in bulk in table 
excel_file = pd.ExcelFile('Superstore_USA.xlsx')
excel_dataframe = excel_file.parse(sheet_name="Orders")
excel_dataframe.to_sql("superstore_orders", conn, if_exists="replace")
# %%
excel_dataframe = excel_file.parse(sheet_name="Returns")
excel_dataframe.to_sql("superstore_returns", conn, if_exists="replace")
excel_dataframe = excel_file.parse(sheet_name="Users")
excel_dataframe.to_sql("superstore_users", conn, if_exists="replace")
# %%
collection = database["superstore_orders"]
collection.insert_many(df_orders.to_dict(orient='records'))
collection = database["superstore_returns"]
collection.insert_many(df_returns.to_dict(orient='records'))
collection = database["superstore_users"]
collection.insert_many(df_users.to_dict(orient='records'))
# %%
#3 . Find out how return that we have received and with a product id
# this cannot be done as the returns sheet, order id is not available in orders sheet. 
# there is no product id in returns sheet too
#4 . try  to join order and return data both in sql and pandas 
# this cannot be done as returns sheet, order id is not available in orders sheet
# %%
#5 . Try to find out how many unique customer that we have 
df_orders['Customer ID'].unique().size
df_orders['Customer Name'].unique().size
# %%
cursor.execute('select count(distinct `Customer Id`) from superstore_orders')
print(cursor.fetchall())
cursor.execute('select count(distinct `Customer Name`) from superstore_orders')
print(cursor.fetchall())
# %%
collection = database["superstore_orders"]
len(collection.distinct('Customer ID'))
len(collection.distinct('Customer Name'))
# %%
#6 . try to find out in how many regions we are selling a product 
# and who is a manager for a respective region 
df1 = pd.merge(df_orders,df_users,on='Region')

# %%
df2 = df1[['Product Name','Region','Manager']].drop_duplicates().sort_values('Product Name')
#%%
df2
# %%
cursor.execute("select distinct `product name`, t1.region, t2.manager from superstore_orders t1 \
    inner join superstore_users t2 on t1.region = t2.region order by 1")
print(cursor.fetchall())
# %%
collection1 = database["superstore_orders"]
collection2 = database["superstore_users"]
result = collection1.aggregate([
    {
     '$lookup': 
     {
        'from' : "superstore_users",
        'localField': "Region",
        'foreignField': "Region",
        'as' : "OrderUser"
    }
    }
    ])

collection3 = database["OrderUser"]
collection3.insert_many(result)
# %%
for i in result:
    print(i)
# %%
a = collection3.find({},{'Product Name':1,'OrderUser':1})
# %%
for i in a:
    print(i)
# %%
#7 . find out how many different differnet shipement mode that we have and what is a percentage usablity 
# of all the shipment mode with respect to dataset 

x = df_orders.groupby('Ship Mode').size().to_frame('count')
# %%
x['usability'] = x['count']/x['count'].sum()*100
x
# %%
#8 . Create a new coulmn and try to find our a diffrence between order date and shipment date
df_orders['shipping delay'] = df_orders['Ship Date'] - df_orders['Order Date']
df_orders['shipping delay']
# %%
#9 . base on question number 8 find out for which order id we have shipment duration more than 10 days 
df_orders[df_orders['shipping delay'] > '10 days']['Order ID']
# %%
#10 . Try to find out a list of a returned order which 
# sihpment duration was more then 15 days and find out that region manager as well 
# %%
#info not available
#11 . Gorup by region and find out which region is more profitable 
df1['shipping delay'] = df1['Ship Date'] - df1['Order Date']
# %%
df1.groupby('Region')['Profit'].sum()
# %%
#12 . Try to find out overalll in which country we are giving more didscount 
df1.groupby('State or Province')['Discount'].sum()
# %%
#13 . Give me a list of unique postal code 
df1['Postal Code'].unique().tolist()
# %%
#14 . which customer segement is more profitalble find it out .
df1.groupby('Customer Segment')['Profit'].sum().sort_values().sort_values(ascending=False).to_frame().iloc[0]
# %%
#15 . try to find out the 10th most loss making product catagory . 
df1.groupby('Product Sub-Category')['Profit'].sum().sort_values().to_frame().iloc[9]
# %%
#16 . Try to find out 10 top  product with highest margins 
df1.groupby('Product Sub-Category')['Product Base Margin'].sum().sort_values(ascending=False).to_frame().iloc[:10]
# %%
df1.groupby('Product Sub-Category')['Product Base Margin'].sum().sort_values(ascending=False).to_frame()
# %%
