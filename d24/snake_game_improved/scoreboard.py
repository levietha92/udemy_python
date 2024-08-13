from turtle import Turtle, Screen
from snake import HALF_SIZE
import os

ALIGN = "center"
FONT = "Courier"
FONTSIZE = 20
FONTTYPE = "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score = 0
        with open("./data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.setx(0)
        self.sety(HALF_SIZE-20)
        self.update_text()    
        self.hideturtle()
        self.goto(0,HALF_SIZE-30)

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {int(self.high_score)}", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
    
    def add_score(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
        self.clear()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("./data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_text()
        
# with open("./data.txt") as file:
#     print(file.read())

# with open("./data.txt", mode="w") as file:
#     file.write("0")    