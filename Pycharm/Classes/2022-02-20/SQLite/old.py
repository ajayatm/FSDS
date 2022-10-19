dbcursor.execute('create table class(name text, batchid int, marks real)')


dbcursor.execute("insert into class values('ajay', 12345, 50)")

db.commit()
obj = dbcursor.execute('select * from class')
print(obj)

for i in obj:
    print(i)

obj = dbcursor.execute('select * from class where marks > 40')
print(obj)

for i in obj:
    print(i)


db = sqlite3.connect('FSDS.db')
dbcursor = db.cursor()
db.close()


