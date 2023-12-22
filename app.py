
# from flask import Flask
from flask_bootstrap import Bootstrap
# from flask import jsonify
import json
from datetime import timedelta
from flask import Flask, jsonify, request,render_template
import MySQLdb as my

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] =  'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] =  'zochitika_db'
# mysql = MySQL(app)
# db = MySQLdb.connect('Darlingson.mysql.pythonanywhere-services.com', 'username-of-db', 'password-of-db', 'database-name')


db = my.connect ('Darlingson.mysql.pythonanywhere-services.com','Darlingson','shinobi4313','Darlingson$default')
db.ping(True)
cursor = db.cursor ()

def connectDB():
    db = my.connect('Darlingson.mysql.pythonanywhere-services.com', 'Darlingson', 'shinobi4313', 'Darlingson$default')
    db.ping(True)
    # cursor = db.cursor()]
    return db
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/analytics')
def analytics():
    return render_template('analyticsApp.html')
@app.route('/compare_team',methods = ['GET'])
def compare_team():
    return render_template('compare_team.html')
@app.route('/compare_players',methods =['GET'])
def compare_players():
    return render_template('compare_players.html')
@app.route('/teams',methods=['GET'])
def getteams():
    data = json.load(open('/home/Darlingson/mysite/2023superLeagueteams.json'))
    return jsonify(data), 200, {"Access-Control-Allow-Origin": "*"}
@app.route('/stats')
def stats():
    data = json.load(open('/home/Darlingson/mysite/csvjson.json'))
    return jsonify(data), 200, {"Access-Control-Allow-Origin": "*"}
    #return jsonify(data)

@app.route("/zochitika")
def getZochitikaAll():
    # cur = mysql.connection.cursor()
    con = connectDB()
    cur = con.cursor()
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
    # cur = mysql.connection.cursor()
    cur = db.cursor ()
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
    # cur = mysql.connection.cursor()
    cur = db.cursor ()
    cur.execute("SELEC/T * FROM zochitika WHERE title LIKE %s OR description LIKE %s",('%' + keyword + '%', '%' + keyword + '%',))
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
    # cur = mysql.connection.cursor()
    cur = db.cursor ()
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