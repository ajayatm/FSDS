import pymongo

client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = { 'name':'ajay',"yob":1981,'height':170,'weight':78}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
