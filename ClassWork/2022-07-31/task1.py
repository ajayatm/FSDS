# %%
import csvkit
import mysql.connector as connection
import pandas as pd
import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")

mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(buffered=True)
cursor.execute('USE FSDS')
#Task 1 - Fitbit Dataset
# %%
#1. Read this dataset in pandas , mysql and mongodb
#2. while creting a table in mysql dont use manual approach to create it,always use a automation to create a table in mysql
df = pd.read_csv('FitBit data.csv')
#csvsql --db "mysql://root:Porsche*911@localhost:3306/FSDS" --tables fitbit_data --insert 'FitBit data.csv'
database = client['mongotest']
collection = database["fitbit_data"]
collection.insert_many(df.to_dict(orient='records'))
# %%
#3. convert all the dates avaible in dataset to timestamp format in pandas 
# and in sql you to convert it in date format
df['DateFormat'] = pd.to_datetime(df['ActivityDate'])
cursor.execute('describe fitbit_data')
print(cursor.fetchall())
# %%
collection.aggregate([{"$project": {"ActivityDate": { "$toDate": "$ActivityDate" }}} ])
# %%
#4 . Find out in this data that how many unique id's we have
df['Id'].unique().size
cursor.execute('select count(distinct id) from fitbit_data')
print(cursor.fetchall())
len(collection.distinct('Id'))
# %%
#5 . which id is one of the active id that you have in whole dataset 
df1 = df.groupby('Id')['TotalSteps'].sum().to_frame()
print(df1[df1['TotalSteps'] == df1['TotalSteps'].max()])
cursor.execute('select id, sum(totalsteps) from fitbit_data group by id order by 2 desc limit 1')
print(cursor.fetchall())
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$TotalSteps'}
      } 
  },
  { '$sort': {'sumQ': -1 } },
  { '$limit': 1 }
])
for i in a:
    print(i)
# %%
#6 . how many of them have not logged there activity find out in terms of number of ids
df1 = df.groupby('Id')['TotalSteps'].sum().to_frame()
df1[df1['TotalSteps'] == 0]
# %%
cursor.execute('select id, sum(totalsteps) as sum from fitbit_data group by id having sum = 0')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$TotalSteps'}
      } 
  }
  ])
for i in a:
    if i['sumQ'] == 0:
        print(i['_id'])
# %%
#7 . Find out who is the laziest person id that we have in dataset 
df1 = df.groupby('Id')['TotalSteps'].sum().to_frame()
df2 = df1[df1['TotalSteps'] > 0]
print(df2[df2['TotalSteps'] == df2['TotalSteps'].min()])
cursor.execute('select id, sum(totalsteps) as sum from fitbit_data group by id having sum > 0 order by 2 limit 1')
print(cursor.fetchall())
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$TotalSteps'}
      } 
  },
  { '$sort': {'sumQ': 1 } }
])
for i in a:
    if i['sumQ'] > 0:
        print(i)
        break
# %%
#8 . Explore over an internet that how much calories burn is required for a healthy person and 
# find out how many healthy person we have in our dataset 
df3 = df.groupby('Id')['Calories'].mean().to_frame()
df3[df3['Calories'] > 2000]
# %%
cursor.execute('select id, avg(calories) as avg from fitbit_data group by id having avg > 2000')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'avgQ': {'$avg': '$Calories'}
      } 
  }
  ])
for i in a:
    if i['avgQ'] > 2000:
        print(i)
# %%
#9. how many person are not a regular person with respect to activity try to find out those 
df4 = df.groupby('Id').size().to_frame('size')
df4[df4['size'] < 10]
# %%
cursor.execute('select id, count(id) as count from fitbit_data group by id having count < 10')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'count': {'$sum': 1}
      } 
  }
  ])
for i in a:
    if i['count'] < 10:
        print(i)
# %%
#10 . who is the thired most active person in this dataset find out those in pandas and in sql both.
df1 = df.groupby('Id')['TotalSteps'].sum().to_frame().sort_values(by='TotalSteps', ascending=False)
print(df1.iloc[[2]])
# %%
cursor.execute('select id, sum(totalsteps) as sum from fitbit_data group by id having sum > 0 order by 2 desc limit 2,1')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$TotalSteps'}
      } 
  },
  { '$sort': {'sumQ': -1 } },
  { '$skip' : 2 },
  { '$limit': 1 }
])
for i in a:
    print(i)
# %%
#11 . who is the 5th most laziest person avilable in dataset find it out 
df1 = df.groupby('Id')['TotalSteps'].sum().to_frame().sort_values(by='TotalSteps')
print(df1.iloc[[4]])
# %%
cursor.execute('select id, sum(totalsteps) as sum from fitbit_data group by id having sum > 0 order by 2 limit 3,1')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$TotalSteps'}
      } 
  },
  { '$sort': {'sumQ': 1 } },
  { '$skip' : 4 },
  { '$limit': 1 }
])
for i in a:
    print(i)

# %%
#12 . what is a totla acumulative calories burn for a person find out
print(df.groupby('Id')['Calories'].sum().to_frame())
# %%
cursor.execute('select id, sum(calories) from fitbit_data group by id')
print(cursor.fetchall())
# %%
a = collection.aggregate([
  { '$group': {
         '_id': '$Id',
         'sumQ': {'$sum': '$Calories'}
      } 
  }
])
for i in a:
    print(i)
# %%
