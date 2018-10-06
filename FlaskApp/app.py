from flask import Flask, render_template, request
app = Flask(__name__)

app.debug = True

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