import sqlite3

db = sqlite3.connect('person.db')
c = db.cursor()

c.execute('create table if not exists v(valuedata text)')
c.execute('delete from v')
db.commit()

f = open('vocab.kos.txt', 'r+', encoding='utf-8')
g = f.readlines()

for line in g:
    b = line.strip()
    b = b.replace(',', " ")
    b = b.replace("'", " ")
    c.execute(f"insert into v values('{b}')")
f.close()

db.commit()

for i in c.execute('select count(*), substr(valuedata, 1, 1) from v group by 2'):
    print(i)
