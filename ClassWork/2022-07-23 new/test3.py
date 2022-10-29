import pymongo
client = pymongo.MongoClient("mongodb+srv://ajayatm3456:Porsche911@cluster0.pu72r.mongodb.net/?retryWrites=true&w=majority")

d =  [
    {
        "_id": {
                "oid": "5968dd23fc13ae04d9000001"
                },
        "product_name": "sildenafil citrate",
        "supplier": "Wisozk Inc",
        "quantity": 261,
        "unit_cost": "$10.47"
    }, 
    {
        "_id": {
                "oid": "5968dd23fc13ae04d9000002"
                },
        "product_name": "Mountain Juniperus ashei",
        "supplier": "Keebler-Hilpert",
        "quantity": 292,
        "unit_cost": "$8.74"
    },
    {
        "_id": {
                "oid": "5968dd23fc13ae04d9000003"
                },
        "product_name": "Dextromathorphan HBr",
        "supplier": "Schmitt-Weissnat",
        "quantity": 211,
        "unit_cost": "$20.53"
    }
    ]

database = client['mongotest']
collection = database["test3"]
#collection.insert_many(d)

#record = collection.find({'quantity':{'$gte':261},'unit_cost':{'$eq':'$10.47'}})
#record = collection.find({'$or':[{'quantity':{'$gte':261}},{'unit_cost':{'$eq':'$20.53'}}]})

record = collection.find({'_id':{'oid': '5968dd23fc13ae04d9000002'}})
for i in record:
    print(i)
