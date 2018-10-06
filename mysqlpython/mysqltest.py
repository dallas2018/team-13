import mysql.connector

cnx = mysql.connector(user='team', password = 'team13', database = 'team13db')

cursor = cnx.cursor()

cursor.execute("""CREATE TABLE Personal (
	email varchar(50) NOT NULL PRIMARY KEY,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    address varchar(50),
    city varchar(50),
    state varchar(50),
    postal_code int,
    county varchar(50),
    DOB date,
    home_phone varchar(20),
    cell_phone varchar(20),
    work_phone varchar(20),
    ssn int,
    facebook text,
    twitter text,
    linkedIn text,
    emergency_contact varchar(30),
    e_relationship varchar(30),
    e_cell varchar(20),
    e_address TEXT
)""")

cnx.close()
