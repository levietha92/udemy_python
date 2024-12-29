from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/") #homepage/
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye") #homepage/bye
def bye():
    return "<b>BYEEEE</b>"

@app.route("/user/<name>/<int:number>")
def greet(name, number):
    return f"Hola {name} boo, you are {number} yrs old"

if __name__=="__main__":
    app.run(debug=True)