from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'team'
app.config['MYSQL_DATABASE_PASSWORD'] = 'team13'
app.config['MYSQL_DATABASE_DB'] = 'team13db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

def insert_personal(args):
    query = "Insert into personal(email, first_name, last_name, dob, ssn) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query,args)

def insert_Contact_Info(args):
    query = "Insert into Contact_Info(email, address, city, state, postal_code, county, phone) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, args)

def insert_Demographic_Info(args):
