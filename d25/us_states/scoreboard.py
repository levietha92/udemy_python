
from turtle import Turtle

FONT = ("Arial",12,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(350,350)
        
    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="right", font=("Arial",30,"normal"))

    def add_score(self):
        self.score += 1