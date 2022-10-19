import sqlite3

db = sqlite3.connect('person.db')
c = db.cursor()
#c.execute('create table person_table(name text, emailid text, age int, salary real)')

#c.execute('insert into person_table values("ajay", "ajayatm@gmail.com", 41, 140000)')
#c.execute('insert into person_table values("sagini", "saginijoy@gmail.com", 37, 180000)')
#c.execute('insert into person_table values("michelle", "michelle.gr2@gmail.com", 7, 0)')
#db.commit()

#data = c.execute('create table dress(name text, dress_name text, dress_color text)')

# c.execute("insert into dress values('ajay', 'shirt', 'blue')")
# c.execute("insert into dress values('ajay', 'shirt', 'white')")
# c.execute("insert into dress values('ajay', 'shirt', 'red')")
# c.execute("insert into dress values('ajay', 'pants', 'black')")
# c.execute("insert into dress values('ajay', 'pants', 'navy')")
# c.execute("insert into dress values('sagini', 'blouse', 'pink')")
# c.execute("insert into dress values('sagini', 'blouse', 'cream')")
# c.execute("insert into dress values('sagini', 'blouse', 'red')")
# c.execute("insert into dress values('sagini', 'skirt', 'black')")
# c.execute("insert into dress values('sagini', 'skirt', 'green')")
# c.execute("insert into dress values('michelle', 'shirt', 'white')")
# c.execute("insert into dress values('michelle', 'shirt', 'blue')")
# c.execute("insert into dress values('michelle', 'skirt', 'blue')")
# c.execute("insert into dress values('michelle', 'skirt', 'black')")
# c.execute("insert into dress values('michelle', 'gown', 'magenta')")
# db.commit()

# data = c.execute('select * from person_table')
# for i in data:
#     print(i)
# data = c.execute('select * from dress')
# for i in data:
#     print(i)
#
# c.execute('create table person_table(name text, emailid text, age int, salary real)')
#
# c.execute('insert into person_table values("ajay", "ajayatm@gmail.com", 41, 140000)')
# c.execute('insert into person_table values("sagini", "saginijoy@gmail.com", 37, 180000)')
# c.execute('insert into person_table values("michelle", "michelle.gr2@gmail.com", 7, 0)')
# db.commit()
# data = c.execute('select * from person_table p left join dress d on p.name = d.name')
# for i in data:
#     print(i)
# print('-------------------------------------------------------------------------------')
# data = c.execute('select * from dress d left join person_table p on p.name = d.name')
# for i in data:
#     print(i)
# c.execute('delete from person_table where age < 10')
# db.commit()
for i in c.execute('select * from person_table'):
    print(i)
c.execute('update person_table set salary = 150000 where salary = 140000')
for i in c.execute('select * from person_table'):
    print(i)
