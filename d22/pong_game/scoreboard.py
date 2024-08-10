from turtle import Turtle, Screen
from pong import HALF_SIZE

ALIGN = "center"
FONT = "Courier"
FONTSIZE = 20
FONTTYPE = "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setx(0)
        self.sety(HALF_SIZE-20)
        self.update_text()    
        self.hideturtle()

    def update_text(self):
        self.write(f"Score = {self.score}", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))