from turtle import Turtle
import random
from paddle import SCREEN_SIZE, HALF_SIZE

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.speed(0)
        pong_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        pong_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        self.penup()
        self.goto(pong_x,pong_y)


    def refresh(self):
        pong_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        pong_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        # self.penup()
        self.goto(pong_x,pong_y)
