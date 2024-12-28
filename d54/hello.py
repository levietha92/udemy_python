from flask import Flask

app = Flask(__name__)

@app.route("/") #homepage/
def hello_world():
    return "Hello, World!"

@app.route("/bye") #homepage/
def hello_world():
    return "BYEEEE"

