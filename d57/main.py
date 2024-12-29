from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
random_number = random.randint(0,100)
current_year = datetime.date.today().year

@app.route('/')
def home():
    return render_template('index.html', 
                           num=random_number,
                           current_year=current_year
                           )
@app.route('/<name>')
def guess(name):
    gender_url=f'https://api.genderize.io?name={name}'
    age_url=f'https://api.agify.io?name={name}'
    
    return render_template('guess.html',
                           name=name,
                           request_gender= requests.get(gender_url),
                           request_age = requests.get(age_url)
                           )
    

if __name__ == "__main__":
    app.run(debug=True)


