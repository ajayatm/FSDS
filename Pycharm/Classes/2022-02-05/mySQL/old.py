class Connection:
    import mysql.connector as conn
    mydb = conn.connect(host='localhost', user='root', password='Porsche*911')
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS firstmysql')
    cursor.execute('SHOW DATABASES')
    print(cursor.fetchall())
    query = 'CREATE TABLE IF NOT EXISTS firstmysql.maintable ' \
            '(studentid INT(10), firstname VARCHAR(30), lastname VARCHAR(30), regid INT(10), classname VARCHAR(30))'
    cursor.execute(query)
    cursor.execute('USE firstmysql')
    cursor.execute('SHOW TABLES')
    print(cursor.fetchall())
    cursor.execute('DELETE from firstmysql.maintable')
    cursor.execute('INSERT INTO firstmysql.maintable values (123123, "Ajay", "Mani", 12312312, "FSDS")')
    cursor.execute('INSERT INTO firstmysql.maintable values (345456, "Sagini", "Kunnel", 67867867, "FSDS")')
    mydb.commit()
    cursor.execute('select * from firstmysql.maintable')
    print(cursor.fetchall())
    cursor.execute('CREATE TABLE IF NOT EXISTS firstmysql.glassdata '
                   '(col1 INT(5), col2 float(10,5), col3 float(10,5), col4 float(10,5), col5 float(10,5),'
                   'col6 float(10,5), col7 float(10,5), col8 float(10,5), col9 float(10,5), col10 float(10,5),'
                   'col11 INT(5))'
                   )

    cursor.execute('INSERT INTO firstmysql.glassdata values (1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)')
    mydb.commit()
    cursor = mydb.cursor()
    cursor.execute('DELETE FROM firstmysql.glassdata')
    with open('glass.data', 'r') as f:
        glass_data = csv.reader(f, delimiter='\n')
        for i in glass_data:
            cursor.execute(f'INSERT INTO firstmysql.glassdata values({i[0]})')

    mydb.commit()
    cursor.execute('SELECT * FROM firstmysql.glassdata')

    for i in cursor.fetchall():
        print(i)