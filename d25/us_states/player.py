from turtle import Turtle
from scoreboard import FONT
import time

class Player(Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)

    def wrong_answer(self):
        self.write("It doesn't exist, Try again", False, align="center", font=FONT)
        time.sleep(0.5)
        self.clear()

    def duplicate_answer(self):
        self.write("You already entered that", False, align="center", font=FONT)
        time.sleep(0.5)
        self.clear()

    def correct_answer(self, text):
        self.write(text, False, align="center", font=FONT)