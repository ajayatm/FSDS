import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")
try:
    database = client['mongotest']
    collection = database["student"]
    f = collection.find()
    print(f)
    g = []
    for i in f:
        print(i)
        g.append(i)
    print(g)
except:
    print('wrong')