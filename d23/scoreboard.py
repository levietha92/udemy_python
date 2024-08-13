from turtle import Turtle
from car_manager import HALF_SIZE

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,HALF_SIZE-50)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", FONT)
