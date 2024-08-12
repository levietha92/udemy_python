from turtle import Turtle
from paddle import HALF_SIZE, MOVE_DISTANCE
import random


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        # self.pong = Turtle(shape='circle')
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(1)
        random_coordinate = random.randrange(-10,10)
        self.x_move = random_coordinate
        self.y_move = random_coordinate
        
    def move(self):
        new_x = self.xcor() + self.x_move # if use self.pong here --> it doesn't affect the x,y cor
        new_y = self.ycor() + self.y_move # if use self.pong here --> it doesn't affect the x,y cor
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x_move *= -1 #this will alter the above because we have pong.move() still ongoing

    def bounce_y(self):
        self.y_move *= -1 #this will alter the above because we have pong.move() still ongoing

    def bounce(self): #this didn't work too well but theoretically I could use angle change to direct the pong
        new_heading = self.heading() + 90
        self.setheading(new_heading)
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(0,0)

