# from flask import Flask
from datetime import timedelta

from flask_mysqldb import MySQL
from flask import Flask, jsonify


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


if __name__ == '__main__':
    app.run(debug=True,port=8085)
