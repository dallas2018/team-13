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

cursor.execute("""DROP TABLE IF EXISTS Personal""")

cursor.execute("""CREATE TABLE Personal (
	email varchar(50) NOT NULL PRIMARY KEY,
    first_name varchar(30) NOT NULL,
	middle_name varchar(30),
    last_name varchar(30) NOT NULL,
	dob varchar(20),
	ssn varchar(20)
	)""")

cursor.execute("DROP TABLE IF EXISTS Contact_Info")

cursor.execute("""CREATE TABLE Contact_Info (
	email varchar(50) NOT NULL PRIMARY KEY,
	address varchar(50),
	city varchar(50),
    state varchar(50),
    postal_code varchar(20),
    county varchar(50),
    phone varchar(20)
	)""")

cursor.execute("DROP TABLE IF EXISTS Demographic_Info")

cursor.execute("""CREATE TABLE Demographic_Info (
	email varchar(50) NOT NULL PRIMARY KEY,
	male boolean,
	female boolean,
	white boolean,
	black boolean,
	asian boolean,
	hispanic boolean,
	hnpi boolean,
	other_race boolean,
	african boolean,
	chinese boolean,
	german boolean,
	japanese boolean,
	persian boolean,
	russian boolean,
	vietnamese boolean,
	na boolean,
	arabic boolean,
	french boolean,
	italian boolean,
	korean boolean,
	potuguese boolean,
	spanish boolean,
	other_languages boolean
)""")

cursor.execute("""DROP TABLE IF EXISTS Work_Auth""")

cursor.execute("""CREATE TABLE Work_Auth (
	email varchar(50) NOT NULL PRIMARY KEY,
	citizenship boolean,
	noncitizenship boolean,
	valid_id boolean,
	transportation varchar(50),
	homeowner varchar(40)
)""")

cursor.execute("""DROP TABLE IF EXISTS Youth""")

cursor.execute("""CREATE TABLE Youth(
	email varchar(50) NOT NULL PRIMARY KEY,
	foster boolean,
	p_incarcerate boolean,
	juvie boolean,
	p_single boolean,
	fr_lunch boolean,
	drop_out boolean,
	parent boolean,
	lack_work boolean
)""")

cursor.execute("""DROP TABLE IF EXISTS Appointment""")


#cursor.execute("""CREATE TABLE Appointment
#	()""")


cursor.execute("""DROP TABLE IF EXISTS Household""")

cursor.execute("""CREATE TABLE Household(
	email varchar(50) NOT NULL PRIMARY KEY,
	marital_status boolean,
	children int,
	young_adults int,
	adults int
)""")

cursor.execute("""DROP TABLE IF EXISTS Finance""")

cursor.execute("""CREATE TABLE Finance(
	email varchar(50) NOT NULL PRIMARY KEY,
	checking boolean,
	savings boolean,
	payday boolean,
	car_title boolean,
	income int,
	public_assist boolean
)""")

cursor.execute("""DROP TABLE IF EXISTS Background""")

cursor.execute("""CREATE TABLE Background(
	email varchar(50) NOT NULL PRIMARY KEY,
	education varchar(20),
	attending_school boolean,
	computer int,
	english int,
	certificated text,
	military varchar(40),
	convicted boolean,
	incarcerated boolean
)""")

cursor.execute("""DROP TABLE IF EXISTS Job1""")
cursor.execute("""DROP TABLE IF EXISTS Job2""")
cursor.execute("""DROP TABLE IF EXISTS Job3""")

cursor.execute("""CREATE TABLE Job1(
	email varchar(50) NOT NULL PRIMARY KEY,
	title text,
	employer text,
	job_type text,
	commitment text,
	start text,
	end_date text,
	wage float,
	hours int,
	supervisor text,
	address text,
	reason text
)""")

cursor.execute("""CREATE TABLE Job2(
	email varchar(50) NOT NULL PRIMARY KEY,
	title text,
	employer text,
	job_type text,
	commitment text,
	start text,
	end_date text,
	wage float,
	hours int,
	supervisor text,
	address text,
	reason text
)""")

cursor.execute("""CREATE TABLE Job3(
	email varchar(50) NOT NULL PRIMARY KEY,
	title text,
	employer text,
	job_type text,
	commitment text,
	start text,
	end_date text,
	wage float,
	hours int,
	supervisor text,
	address text,
	reason text
)""")

cursor.execute("""DROP TABLE IF EXISTS Needs""")

cursor.execute("""CREATE TABLE Needs(
	email varchar(50) NOT NULL PRIMARY KEY,
	interests text,
	availability varchar(30),
	investment varchar(30),
	getting_job text,
	wage_exp varchar(20),
	durg_test boolean
)""")

cursor.execute("""DROP TABLE IF EXISTS Questions""")

cursor.execute("""CREATE TABLE Questions(
	email varchar(50) NOT NULL PRIMARY KEY,
	church_flyer boolean,
	church_presentation boolean,
	community_flyer boolean,
	community_agency boolean,
	guidance_counselor boolean,
	hcc boolean,
	information_session boolean,
	internet boolean,
	job_fair boolean,
	ser_client boolean,
	united_way boolean,
	workforce boolean
)""")

conn.commit()

conn.close()
