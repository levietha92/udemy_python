from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

print(__name__) # shows __main__

#this below is alternative to setting `export FLASK_APP=hello.py`
if __name__=='__main__':
    app.run()
