from turtle import Turtle, Screen
from snake import HALF_SIZE

ALIGN = "center"
FONT = "Courier"
FONTSIZE = 20
FONTTYPE = "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.setx(0)
        self.sety(HALF_SIZE-20)
        self.update_text()    
        self.hideturtle()
        self.goto(0,HALF_SIZE-30)

    def update_text(self):
        self.clear()
        self.write(f"Score = {self.score}, Highest score = {self.high_score}", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
    
    def add_score(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align=ALIGN, font=(FONT, FONTSIZE, FONTTYPE))
        self.clear()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_text()
        