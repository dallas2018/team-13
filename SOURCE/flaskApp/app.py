from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('1')
def one():
    return render_template('1')


if __name__ == "__main__":
    app.run()

