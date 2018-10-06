from flask import Flask, render_template, request
#import send_email
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


if __name__== "__main__":
    app.run()


@app.route('/test')
def test():

    _name = request.form['']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

