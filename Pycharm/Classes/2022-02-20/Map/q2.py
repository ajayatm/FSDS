import sqlite3

db = sqlite3.connect('person.db')
c = db.cursor()

for i in c.execute('select count(*), substr(valuedata, 1, 1) from v group by 2'):
    print(i)

# c.execute('create table if not exists v(valuedata text)')
#
# f = open('vocab.nytimes.txt', 'r+', encoding='utf-8')
# g = f.readlines()
#
# for line in g:
#     b = line.strip()
#     c.execute(f"insert into v values('{b}')")
# f.close()

# db.commit()