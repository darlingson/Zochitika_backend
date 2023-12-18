# from flask import Flask
from datetime import timedelta

from flask_mysqldb import MySQL
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'zochitika_db'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)
# app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route("/zochitika")
def getZochitikaAll():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM zochitika")
    rv = cur.fetchall()
    json_data = []
    row_headers = [x[0] for x in cur.description] #extracting row headers
    for result in rv:
        row_data = dict(zip(row_headers,result))
        for key, value in row_data.items():
            if isinstance(value, timedelta):
                # convert timedelta to string
                row_data[key] = str(value)
        json_data.append(row_data)
    return jsonify(json_data)
    # return str(rv)
@app.route("/zochitika/<id>")
def getZochitikaById(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM zochitika WHERE id = %s", (id,))
    rv = cur.fetchall()
    json_data = []
    row_headers = [x[0] for x in cur.description] #extracting row headers
    for result in rv:
        row_data = dict(zip(row_headers,result))
        for key, value in row_data.items():
            if isinstance(value, timedelta):
                # convert timedelta to string
                row_data[key] = str(value)
        json_data.append(row_data)
    return jsonify(json_data)

@app.route("/zochitika/search")
def searchZochitika():
    keyword = request.args.get('keyword')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM zochitika WHERE title LIKE %s OR description LIKE %s",('%' + keyword + '%', '%' + keyword + '%',))
    rv = cur.fetchall()
    json_data = []
    row_headers = [x[0] for x in cur.description] #extracting row headers
    for result in rv:
        row_data = dict(zip(row_headers,result))
        for key, value in row_data.items():
            if isinstance(value, timedelta):
                # convert timedelta to string
                row_data[key] = str(value)
        json_data.append(row_data)
    return jsonify(json_data)

@app.route("/zochitika/filter")
def filterZochitika():
    date = request.args.get('date')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM zochitika WHERE date = %s", (date,))
    rv = cur.fetchall()
    json_data = []
    row_headers = [x[0] for x in cur.description] #extracting row headers
    for result in rv:
        row_data = dict(zip(row_headers,result))
        for key, value in row_data.items():
            if isinstance(value, timedelta):
                # convert timedelta to string
                row_data[key] = str(value)
        json_data.append(row_data)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True,port=8085)
