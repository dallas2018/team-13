from flask import Flask, render_template, request
app = Flask(__name__)

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

@app.route('/household',method=['POST'])
def household():
    marital_status = request.form['Marital Status']
    child17Under = request.form['Children 17 and Under']
    youngAdults = request.form['Young Adults 18-24']
    adults = request.form['Adults']

@app.route('/finance',method=['POST'])
def finance():
    checking = request.form['Checking']
    saving = request.form['Saving']
    paydayLoan = request.form['Payday Loan']
    carTitle = request.form['Car Title Loan']
    householdIncome = request.form['Household Income']
    publicAssistance = request.form['Public Assistance Benefits Programs']

@app.route('/clientBackground',method=['POST'])
def clientBackground():
    educationLevel = request.form['Highest Level of Education']
    currentlyAttending = request.form['Currently Attending School']
    paydayLoan = request.form['Payday Loan']
    computerSkills = request.form['Computer Skills']
    englishLiteracy = request.form['English Literacy Level']
    certs = request.form['Certificates/Training']
    militaryStatus = request.form['Military Status']
    criminal = request.form['Criminal Status']



if __name__ == "__main__":
    app.run()
