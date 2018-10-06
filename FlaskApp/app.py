from flask import Flask, render_template, request
import json
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
    homeowner = request.form['Homeowner']
    youthQuestions = request.form['Youth Questions']

@app.route('/appt',methods=['POST'])
def appt():
    avail = request.form['Availability']
    contactPref = request.form['Contact Preference']

@app.route('/household',methods=['POST'])
def household():
    marital_status = request.form['Marital Status']
    child17Under = request.form['Children 17 and Under']
    youngAdults = request.form['Young Adults 18-24']
    adults = request.form['Adults']

@app.route('/finance',methods=['POST'])
def finance():
    checking = request.form['Checking']
    saving = request.form['Saving']
    paydayLoan = request.form['Payday Loan']
    carTitle = request.form['Car Title Loan']
    householdIncome = request.form['Household Income']
    publicAssistance = request.form['Public Assistance Benefits Programs']

@app.route('/clientBackground',methods=['POST'])
def clientBackground():
    educationLevel = request.form['Highest Level of Education']
    currentlyAttending = request.form['Currently Attending School']
    paydayLoan = request.form['Payday Loan']
    computerSkills = request.form['Computer Skills']
    englishLiteracy = request.form['English Literacy Level']
    certs = request.form['Certificates/Training']
    militaryStatus = request.form['Military Status']
    criminal = request.form['Criminal Status']

@app.route('/employerHistory',methods=['POST'])
def employerHistory():
    empStatus = request.form['Employment Status']
    title1 = request.form['Title 1']
    employer1 = request.form['Employer 1']
    jobType1 = request.form['Job Type 1']
    Commitment1 = request.form['Commitment 1']
    start1 = request.form['Start 1']
    end1 = request.form['End 1']
    wage1 = request.form['Wage 1']
    hoursPerWeek1 = request.form['Hours/wk 1']
    supervisor1 = request.form['Supervisor 1']
    address1 = request.form['Address 1']
    reasonForLeave1 = request.form['Reason For Leaving 1']

    title2 = request.form['Title 2']
    employer2 = request.form['Employer 2']
    jobType2 = request.form['Job Type 2']
    Commitment2 = request.form['Commitment 2']
    start2 = request.form['Start 2']
    end2 = request.form['End 2']
    wage2 = request.form['Wage 2']
    hoursPerWeek2 = request.form['Hours/wk 2']
    supervisor2 = request.form['Supervisor 2']
    address2 = request.form['Address 2']
    reasonForLeave2 = request.form['Reason For Leaving 2']

    title3 = request.form['Title 3']
    employer3 = request.form['Employer 3']
    jobType3 = request.form['Job Type 3']
    Commitment3 = request.form['Commitment 3']
    start3 = request.form['Start 3']
    end3 = request.form['End 3']
    wage3 = request.form['Wage 3']
    hoursPerWeek3 = request.form['Hours/wk 3']
    supervisor3 = request.form['Supervisor 3']
    address3 = request.form['Address 3']
    reasonForLeave3 = request.form['Reason For Leaving 3']

@app.route('/clientNeeds',methods=['POST'])
def clientNeeds():
    Interests = request.form['Interests']
    availability = request.form['Availability for job']
    investment = request.form['Investment in job (How long you plan on staying)']
    whyNotAJob = request.form['What kept you from getting a job and from keeping a job?']
    wageExpec = request.form['Wage expectation']
    drugTest = request.form['Drug test']
    otherQuestions = request.form['Other Questions/Comments']
    howdYouHear = request.form['How did you hear about SER Jobs for Progress?']


@app.route("/")
def render():
    return render_template("index.html")

@app.route("/<path:path>.html")
def fileRouter(path):
    return render_template("/" + path + ".html")


@app.route("/api/<path:path>", methods=['GET', 'POST'])
def process_form(path):
    print(request.form)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run("127.0.0.1", "8080")