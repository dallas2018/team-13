from flask import Flask, render_template, request
app = Flask(__name__)

<<<<<<< HEAD
=======
app.debug = True
>>>>>>> 851f534dcbc55be73ee1a473cbf8baa48a9114bf
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

@app.route('/contactInfo',method=['POST'])
def contactInfo():
    street_address = request.form['Street Address']
    city = request.form['City']
    state = request.form['State']
    postal_code = request.form['Postal Code']
    county = request.form['County']
    postal_code = request.form['Postal Code']
    phone = request.form['Phone']

@app.route('/demographics',method=['POST'])
def demographic():
    gender = request.form['Gender']
    race = request.form['Race']
    languages = request.form['Languages']
    work_auth = request.form['Authorized to Work']
    postal_code = request.form['Postal Code']
    citizenship = request.form['Citizenship']
    validId = request.form['Valid Form of ID']
    transportation = request.form['Transportation']
    homeowner = request.form['Homeowner']
    youthQuestions = request.form['Youth Questions']

@app.route('/appt',method=['POST'])
def appt():
    avail = request.form['Availability']
    contactPref = request.form['Contact Preference']

<<<<<<< HEAD
@app.route('/household',method=['POST'])
def household():
    marital_status = request.form['Marital Status']
    child17Under = request.form['Children 17 and Under']
    youngAdults = request.form['Young Adults 18-24']
    adults = request.form['Adults']



if __name__ == "__main__":
    app.run()
=======
if __name__ == "__main__":
    app.run()
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
            return render_template("index.2.html")
        elif path == "2":
            print("This is of form 2")
        elif path == "3":
            print("This is of form 3")
        else:
            print("We can't accept anything not of path num")
    else:
        print("REQUEST IS NOT POST, UNHANDLED")


if __name__ == "__main__":
    app.run('127.0.0.1', '8080')
>>>>>>> 851f534dcbc55be73ee1a473cbf8baa48a9114bf
