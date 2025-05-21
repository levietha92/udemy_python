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
@app.route('/name/<name>')
def guess(name):
    gender_url=f'https://api.genderize.io?name={name}'
    age_url=f'https://api.agify.io?name={name}'
    
    return render_template('guess.html',
                           name=name,
                           request_gender= requests.get(gender_url),
                           request_age = requests.get(age_url)
                           )
   
@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url='https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts, number=number) 

if __name__ == "__main__":
    app.run(debug=True)


