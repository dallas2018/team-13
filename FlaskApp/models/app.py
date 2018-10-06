from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def render():
    return render_template("index.html")

@app.route("/api")
def process_form():
    rule = request.url_rule
    if "1" in rule:
        return "1"
    if "2" in rule:
        return "2"


if __name__ == "__main__":
    app.run('127.0.0.1', '8080')