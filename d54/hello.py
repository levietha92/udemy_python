from flask import Flask

app = Flask(__name__)

@app.route("/") #homepage/
def hello_world():
    return "Hello, World!"

@app.route("/bye") #homepage/bye
def bye():
    return "BYEEEE"

@app.route("/user/<name>")
def greet(name):
    return f"Hola {name} boo"

if __name__=="__main__":
    app.run(debug=True)