from flask import Flask

app = Flask(__name__)

@app.route("/") #homepage/
def hello_world():
    return "Hello, World!"

@app.route("/bye") #homepage/bye
def bye():
    return "BYEEEE"

@app.route("/user/<name>/<int:number>")
def greet(name, number):
    return f"Hola {name} boo, you are {number} yrs old"

if __name__=="__main__":
    app.run(debug=True)