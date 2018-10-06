from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def render():
    return render_template("index.1.html")

@app.route("/api/<path:path>")
def process_form(path):
    if request.method == 'POST':
        if path == "1":
            print("This is of form 1")
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