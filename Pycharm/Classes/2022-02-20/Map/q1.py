from operator import countOf
import pymongo
from cytoolz import count

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.a8w62.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

coll1 = db['ajay_collection']

for i in coll1.aggregate([{'$group': {'$substring': [{'values': {'$exists': True}}, 0, 1]}, count: {'$sum': 1}}]):
    print(i)

#coll1.delete_many({})

# f = open('vocab.nytimes.txt', 'r+', encoding='utf-8')
# g = f.readlines()
# a = dict()
# print(type(a))
# list1 = []
# count = 0
# for line in g:
#     count += 1
#     b = line.strip()
#     list1.append(b)
# f.close()
#
# a['values'] = list1
# #
# coll1.insert_one(a)

#print(a)
# coll1.insert_one(a)
# for i in coll1.find():
#     print(i)

# x = open('nytimes.txt', 'w', encoding='utf-8')
# x.write(str(a.items()))
# x.close()

# def __eq__(x, y):
#     if x == y:
#         return True
#
#
#print(countOf(a.values(), 2))


#print(list(a.items()))
#
# countlist = pd.Series(list1).value_counts()
# listxxx = []
# for i in countlist:
#     listxxx.append(i)
# print(listxxx)
# x = open('count.txt', 'w')
# x.write(countlist)
# x.close()
