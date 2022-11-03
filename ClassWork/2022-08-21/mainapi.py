from flask import Flask, request, jsonify
import mysql.connector as connection
mydb = connection.connect(host='localhost', user='root',passwd='Porsche*911')
cursor = mydb.cursor(dictionary=True)

app = Flask(__name__)

@app.route('/testfun')
def test():
    get_name = request.args.get("name")
    get_phone = request.args.get("phone")
    return "get function for {} {}".format(get_name, get_phone)

@app.route('/getsql')
def getsql():
    try:
        get_db = request.args.get("database")
        get_tb = request.args.get("table")
        print(get_db)
        print(get_tb)
        cursor.execute(f'select * from {get_db}.{get_tb}')
        x = cursor.fetchall()
        print(x)
        return jsonify(x)
    except Exception as e:
        return jsonify(e)


if __name__ == '__main__':
    app.run(port=9999)