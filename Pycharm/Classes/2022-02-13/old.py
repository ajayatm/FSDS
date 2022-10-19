#print(db)
#print(client.list_database_names())

#d1 = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
#coll1.insert_one(d1)

mylist = [
    {
      "Column 1": "A1",
      "Column 2": "A2",
      "Column 3": "A3"
    },
    {
      "Column 1": "B1",
      "Column 2": "B2",
      "Column 3": "B3"
    },
    {
      "Column 1": "C1",
      "Column 2": "C2",
      "Column 3": "C3"
    }
  ]
coll1.insert_one(mylist)

for i in coll1.find().limit(1):
    print(i)
for i in coll1.find({'1': 'a'}):
    print(i)

for i in coll1.find():
    print(i)

coll1.update_many({'Column 1': 'A1'}, {"$set": {'Column 1': 'Ajay Mani'}})

for i in coll1.find({'A': {'$not': {'$eq': 'A1'}}}):
    print(i)

for i in coll1.find({'1': {'$eq': 'a'}}):
    print(i)

coll1.find_one_and_update({'1': {'$exists': True}}, {'$set': {'4': 'z'}})