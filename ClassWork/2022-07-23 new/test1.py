import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")


d = {
    "data": [
        {
            "MainId": 1111,
            "firstName": "Sherlock",
            "lastName": "Homes",
            "categories": [
                {
                    "CategoryID": 1,
                    "CategoryName": "Example"
                }
            ]
        },
        {
            "MainId": 122,
            "firstName": "James",
            "lastName": "Watson",
            "categories": [
                {
                    "CategoryID": 2,
                    "CategoryName": "Example2"
                }
            ]
        }
    ],
    "messages": [], # blank json
    "success": True # boolean value
}

database = client['mongotest']
collection = database["test"]
#collection.insert_one(d)

record = collection.find()
for i in record:
    print(i)
