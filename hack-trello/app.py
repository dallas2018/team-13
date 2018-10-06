from flask import Flask, render_template, redirect, url_for, request, session
import json
from communication.message import SendMessages

''' Application setup and instantiation of helper classes'''
app = Flask(__name__)
# TODO: generate a unique secret key from a hashing library so that people cannot see our app secret
app.secret_key = ""  # This unique hash is from an online generator

s = SendMessages()
contacts = s.c.contacts
user_dict = {x: True for x in contacts}

@app.route("/",methods=["GET"])
def main():
    #Checks to see if there is an error message from login
    if "message" in request.args:
        login_message = request.args["message"]
        return render_template("index.html",message = login_message)

    return render_template("index.html")

@app.route("/message-page",methods = ["GET"])
def message_page():

    #Checks to see if there is an error message from posting
    if "message" in request.args:
        failed_message = request.args["message"]
        return render_template("message-page.html", members = user_dict, message = failed_message)

    #Checks to see if the user has authenticated. If not, redirect to login page
    if session.get('logged_in') is not None:

        #Redirects to login page
        if session.get('logged_in'):
            return render_template("message-page.html", members = user_dict)

    return redirect(url_for("main"))

@app.route("/confirm-message")
def confirm_message():
    return render_template("confirm-message.html")

@app.route("/handle-login", methods = ["POST"])
def handle_login():
    '''
    Route that handles the login form data and checks to see if users are properly authorized
    :return: Route. Message page.
    '''

    #Check the form parameters and match them with the real_un and real_pw
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        login_creds = []
        with open("login.json","r") as f:
            login_creds = json.load(f)
        try:
            real_pwd = login_creds[username]
        except KeyError:
            return redirect(url_for("main",message = "Please enter a valid username and password combination."))
        else:
            #Redirects user based on the result of the authentication check
            if password == real_pwd:
                #Add them to the session because of successful auth
                session["logged_in"] = True
                return redirect(url_for("message_page"))

            else:
                return redirect(url_for("main",message = "Please enter a valid username and password combination."))

@app.route("/handle-message",methods = ["POST"])
def handle_message():

    if request.method== "POST":
        #Type of social media, "all-msg", "text" , "fb", "email"
        social_media_type = request.form["msg-selector"]

        #List of people or default "all-members"
        people_list = request.form.getlist("member")

        #Default case of people_dict is all users
        #Send message to each person in people_dict
        people_dict = _get_people_message_dict(people_list) if _get_people_message_dict(people_list) else user_dict

        #Perform all messaging here
        if people_dict == user_dict:

            #Checks to see if the batch upload is successful and redirects if not
            try:
                s.send_all_messages(social_media_type)
            except:
                return redirect(url_for("message_page",message = "The batch message could not be sent!"))

        else:
            for person in people_dict:

                #Checks case when messages cannot be send to a person
                try:
                    s.send_indv_message(person, social_media_type)
                except Exception as e:
                    print(e)
                    return redirect(url_for("message_page",message = "A message could not be sent to "+person))

    return redirect(url_for("confirm_message"))

''' Helper functions '''
def _get_people_message_dict(people_list):

    # Checks if it is the default all or specific members are chosen
    if people_list:
        if people_list[0] != "all-members":
            people_dict = {key: value for key, value in user_dict.items() if key in people_list}
            return people_dict

    return None

if __name__ =="__main__":
    app.run()
