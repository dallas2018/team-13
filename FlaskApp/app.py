from flask import Flask, render_template, request
import json
app = Flask(__name__)

app.debug = True
@app.route("/home")
def main():
    return render_template('index.html')

@app.route('/personalInfo', methods=['POST'])
def personalInfo():
    # read the posted values from the UI
    first_name = request.form['First Name']
    middle_name = request.form['Middle Name']
    last_name = request.form['Last Name']
    ssn = request.form['SSN']
    dob = request.form['DOB']
    email = request.form['Email']

@app.route('/contactInfo',methods=['POST'])
def contactInfo():
    street_address = request.form['Street Address']
    city = request.form['City']
    state = request.form['State']
    postal_code = request.form['Postal Code']
    county = request.form['County']
    postal_code = request.form['Postal Code']
    phone = request.form['Phone']

@app.route('/demographics',methods=['POST'])
def demographic():
    gender = request.form['Gender']
    race = request.form['Race']
    languages = request.form['Languages']
    work_auth = request.form['Authorized to Work']
    postal_code = request.form['Postal Code']
    citizenship = request.form['Citizenship']
    validId = request.form['Valid Form of ID']
    transportation = request.form['Transportation']
    homework = request.form['Homeowner']


@app.route("/")
def render():
    return render_template("index.1.html")


@app.route("/api/<path:path>", methods=['GET', 'POST'])
def process_form(path):
    if request.method == 'POST':
        if path == "1":
            _firstname = request.form['firstname']
            _lastname = request.form['lastname']
            print(_firstname, _lastname)
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

        elif path == "2":
            return 

        elif path == "3":
            print("This is of form 3")

        else:
            print("We can't accept anything not of path num")

    else:
        if path == "2":
            return render_template("index.2.html")


if __name__ == "__main__":
    app.run('127.0.0.1', '8080')