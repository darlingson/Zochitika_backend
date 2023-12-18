from flask import Flask
from flask_mysqldb import MySQL

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

    return str(rv)


if __name__ == '__main__':
    app.run(debug=True,port=8085)
