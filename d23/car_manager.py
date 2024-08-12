from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SCREEN_SIZE = 600
HALF_SIZE = SCREEN_SIZE/2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,1.5)
        self.color(random.choice(COLORS))
        car_x = random.randint(HALF_SIZE, HALF_SIZE + 20)
        car_y = random.randint(-HALF_SIZE +50 , HALF_SIZE - 50)
        self.penup()
        self.speed(0)
        self.goto(car_x,car_y)
        self.setheading(180)
        # self.car_list = []
            

    def move(self):
        self.forward(MOVE_INCREMENT)