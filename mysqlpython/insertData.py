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
    query = "Insert into Personal(email, first_name, middle_name, last_name, dob, ssn) VALUES(%s, %s, %s, %s, %s)"
    values = (args["Email"], args["First Name"], args["Middle Name"], args["Last Name"], args["DOB"], args["SSN]"])
    cursor.execute(query, values)

def insert_Contact_Info(email, args):
    query = "Insert into Contact_Info(email, address, city, state, postal_code, county, phone) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (email, args["Street Address"], args["City"], args["State"], args["Postal Code"], args["County"], args["Phone"])
    cursor.execute(query, args)

def insert_Demographic_Info(email, args):
    query = "Insert into Demographic_Info(email, male, female, white, black, asian, hispanic, hnpi, other_race, african, chinese, german, japenese, persoan, russian, vietnamese, na, arabic, french, italian, korean, portuguese, spanish, other_languages) VALUES(%{email}, %{args[""]})"
    cursor.execute(query,args)

def insert_Work_Auth(args):
    query = "Insert into Work_Auth(email, citizenship, noncitizenship, valid_id, transportation, homeowner) VALUES()"
    cursor.execute(query,args)

def insert_Youth(args):
    query = "Insert into Youth(email, foster, p_incarcerate, juvie, p_single, fr_lunch, drop_out, parent, lack_work) VALUES()"
    cursor.execute(query,args)

def insert_Appointment(args):
    query = ""

def insert_Household(args):
    query = "Inserts into Household(email, marital_status, children, young_adults, adults) VALUES()"
    cursor.execute(query,args)

def insert_Finance(args):
    query = "Insert into Finance(email, checking, savings, payday, car_title, income, public_assist) VALUES()"
    cursor.execute(query,args)

def insert_Background(args):
    query = "Insert into Background(email, education, attending_school, computer, english, certificated, military, convicted, incarcerated)"
    cursor.execute(query,args)

def insert_Job(job,args):
    query = "Insert into %{job}(email, title, employer, job_type, commitment, start, end_date, wage, hours. supervis. address, reason) VALUES(),"
    cursor.execute(query,args)

def insert_Needs(args):
    query = "Insert into Needs(email, interests, availability, investment, getting_job, wage_exp, drug) VALUES()"
    cursor.execute(query, args)

def insert_Questions(args):
    query = "Insert into Questions(email, church_flyer, church_presentation, community_flyer, community_agency, guidance counselor, hcc, information_session, interet, job_fair, ser_client, united_way, workforce) VALUES()"
    cursor.execute(query, args)
