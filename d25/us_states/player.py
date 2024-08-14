from turtle import Turtle
from scoreboard import FONT
import time

class Player(Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.wrong_answer_count = 0

    def wrong_answer(self):
        self.color("red")
        self.write("It doesn't exist, Try again", False, align="center", font=FONT)
        time.sleep(0.5)
        self.clear()
        self.wrong_answer_count +=1

    def duplicate_answer(self):
        self.color("red")
        self.write("You already entered that", False, align="center", font=FONT)
        time.sleep(0.5)
        self.clear()
        self.wrong_answer_count +=1

    def correct_answer(self, text):
        self.write(text, False, align="center", font=FONT)

    def game_over(self):
        if self.wrong_answer_count == 5:
            self.color("red")
            self.write("GAME OVER", False, align="center", font=FONT)