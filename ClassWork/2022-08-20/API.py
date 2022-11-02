from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        return jsonify(str(a+b))

@app.route('/abc1',methods=['GET','POST'])
def test1():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        return jsonify(str(a*b))

@app.route('/abc2',methods=['GET','POST'])
def test2():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        return jsonify(str(" "))


if __name__ == '__main__':
    app.run()
