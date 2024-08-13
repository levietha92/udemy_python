from turtle import Turtle
import random
from snake import SCREEN_SIZE

HALF_SIZE = SCREEN_SIZE / 2

# class Food:
#     def __init__(self):
#         food = t.Turtle(shape="circle")
#         food.color("red")
#         food.shapesize(1,1,1)
#         food_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
#         food_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
#         food.penup()
#         food.goto(food_x,food_y)
#         self.xcor = food.xcor()
#         self.ycor = food.ycor()

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed(0)
        food_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        food_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        self.penup()
        self.goto(food_x,food_y)


    def refresh(self):
        food_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        food_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        # self.penup()
        self.goto(food_x,food_y)
