from turtle import Turtle, Screen
from paddle import HALF_SIZE

ALIGN = "center"
FONT = "Courier"
FONTSIZE = 40
FONTTYPE = "bold"

class ScoreBoard(Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.update_text()    
        self.hideturtle()

    def update_text(self):
        self.write(f"{self.score}", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_text()

    