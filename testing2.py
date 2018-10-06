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

cursor.execute("Select * FROM Contact_info")
rows = cursor.fetchall()
for row in rows:
    print("\temail:", row[0], "\taddress:", row[1], "\tcity:", row[2], "\tstate:", row[3]
    , "\tpostal_code:", row[4], "\tcounty:", row[5], "\tphone:", row[6])