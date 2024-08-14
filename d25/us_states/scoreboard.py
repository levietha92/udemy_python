
from turtle import Turtle
import time

FONT = ("Arial",12,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(300,350)
        self.start_time = time.time() #epoch

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}/50", False, align="center", font=("Arial",30,"normal"))

    def add_score(self):
        self.score += 1

    def show_timer(self):
        self.goto(300,300)
        
    def count_down(self):
        counter_duration = 2 * 60 #10 minutes
        self.elapsed_time = time.time() - self.start_time #diff, abs seconds
        # if self.elapsed_time != 0:
        self.time_left = counter_duration - self.elapsed_time 
        self.time_left_c = time.gmtime(self.time_left)
        self.clear()
        self.write(f"Timer: {self.time_left_c.tm_min}:{self.time_left_c.tm_sec}", False, align="center", font=("Arial",30,"normal"))

    def time_up(self):
        if self.time_left <= 0:
            self.goto(0,0)
            self.write(f"TIME UP!", False, align="center", font=("Arial",30,"normal"))
            return True