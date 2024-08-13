from turtle import Turtle
from car_manager import HALF_SIZE

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font=FONT)

    # def level_up(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("Level up!", align= "center", font=FONT)
