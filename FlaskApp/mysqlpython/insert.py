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

cursor.execute("INSERT INTO Personal(email, first_name, last_name) VALUES(%s, %s, %s)",("Ninj", "Jhaveri", "nikun"))

conn.commit()
