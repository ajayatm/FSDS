import pymongo
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.a8w62.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

coll1 = db['ajay_collection']

for i in coll1.find():
    print(i)

coll1.delete_many({'myrows': {'$exists': True}})

for i in coll1.find():
    print(i)
