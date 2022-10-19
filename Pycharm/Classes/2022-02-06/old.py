cursor.execute('SELECT * FROM firstmysql.glassdata WHERE col1 > 210')
print(cursor.fetchall())
cursor.execute('DELETE FROM firstmysql.glassdata WHERE col1 = 214')
mydb.commit()
cursor.execute('SELECT * FROM firstmysql.glassdata WHERE col1 > 210')
print(cursor.fetchall())
cursor.execute('UPDATE firstmysql.glassdata SET col11 = 8, col10 = 10.0 WHERE col1 = 213')
mydb.commit()
cursor.execute('SELECT * FROM firstmysql.glassdata WHERE col1 > 210')
print(cursor.fetchall())
cursor.execute('SELECT count(*), classname from firstmysql.maintable GROUP BY classname')
print(cursor.fetchall())
cursor.execute("SELECT * FROM glassdata WHERE col2 LIKE '1.515%'")
cursor.execute("SELECT * FROM (SELECT col1, col2 FROM glassdata WHERE col2 LIKE '1.515%') AS ABC WHERE col2 < 1.5151")
cursor.execute("CREATE TABLE IF NOT EXISTS car_evaluation "
               "(buying VARCHAR(10), maint VARCHAR(10), doors VARCHAR(10), persons VARCHAR(10),"
               "lug_boot VARCHAR(10), safety VARCHAR(10), class VARCHAR(10))")
with open('car.data.new', 'r') as f:
    car_data = csv.reader(f, delimiter='\n')
    for i in car_data:
        cursor.execute(f'INSERT INTO car_evaluation values({i[0]})')
mydb.commit()
