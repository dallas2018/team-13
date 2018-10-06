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

cursor.execute("Select * FROM Personal")
rows = cursor.fetchall()
for row in rows:
    print("Email:", row[0], "\tFirst name:", row[1], "\tMiddle name:", row[2], "\tlast name:", row[3], "\tdob:", row[4]
          , "\tssn:", row[5])

