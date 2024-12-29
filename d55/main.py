#higher lower, render actual HTML with FLASK

from flask import Flask
import random


question = "Guess a number between 0 and 9"
chosen_number = random.randint(0,9)

app = Flask(__name__)
@app.route("/")
def guess():
  return f'''
    <h1 style="text-align:center">\
      <p> {question} </p>\
      <p> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> </p>\
    </h1>'''
    
@app.route("/<int:number>")
def answer(number):
  # number = user_input(question)  
  if number > chosen_number:
    return f'''
    <h1 style="text-align:center">\
      <p> Too high try again </p>\
      <p> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG91dHdud3ZnZndmM29zcWxudjN6Z3lmdnhyOXZueXM3ZGozMG03eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3OOvKXkY8qwtuHPt1U/giphy.gif"> </p>\
    </h1>'''
  elif number < chosen_number:
    return f'''
    <h1 style="text-align:center">\
      <p> Too low try again </p>\
      <p> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDI0ZWRjdTM3MTZnd3ljcXB6NGpkZ2Z2cHlpN25hMHNraXljMTZ4dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ei3baMfQy3xzje8EhS/giphy.gif"> </p>\
    </h1>'''
  else:
    return f'''
    <h1 style="text-align:center">\
      <p> Woohoo you found me </p>\
      <p> <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExejdoemUzYTZmY2ZnemhzbHN2ajNiaWFhMzNzMzY2bXozc2llYXF1dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/v8Y5lgiv2cOH8ToNjT/giphy.gif"> </p>\
    </h1>'''

if __name__=='__main__':
  app.run(debug=True)