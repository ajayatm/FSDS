import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")

database = client['mongotest']
collection = database["test"]

record = collection.find()
#for i in record:
#    print(i)


#data = collection.find({'success': True})
data = collection.find({'height': {'$gt':100}})
for i in data:
    print(i)

