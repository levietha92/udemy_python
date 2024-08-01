import turtle as t
import random
from snake import SCREEN_SIZE

HALF_SIZE = SCREEN_SIZE / 2

class Food:
    def __init__(self):
        food = t.Turtle(shape="circle")
        food.color("red")
        food.shapesize(1,1,1)
        food_x = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        food_y = random.randrange(-HALF_SIZE+30, HALF_SIZE-30)
        food.penup()
        food.goto(food_x,food_y)
        self.xcor = food.xcor()
        self.ycor = food.ycor()


        

        
