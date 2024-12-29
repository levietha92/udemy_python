from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)
random_number = random.randint(0,100)

@app.route('/')
def home():
    return render_template('index.html', 
                           num=random_number,
                           current_year=datetime.date.today().year
                           )


if __name__ == "__main__":
    app.run(debug=True)


