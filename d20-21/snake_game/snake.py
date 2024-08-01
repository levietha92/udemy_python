import turtle as t
import time
import random

STEPS = 20
SCREEN_SIZE = 600
HALF_SIZE = SCREEN_SIZE / 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.pos = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self, snake_length=3):
        for index in range(0,snake_length):
            pos_unit = -index * STEPS
            self.pos.append(pos_unit)
            square = t.Turtle(shape="square")
            square.penup()
            square.color("white")
            square.setx(self.pos[index])
            square.sety(0)
            square.speed(0)
            self.snake.append(square)

    def move(self):
        for index in range(len(self.snake)-1,0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
            self.head.forward(STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


# I was thinking about how on earth can I combine the snake_length and food being eaten in 1 go
# Day 21 resolves this with Class Inheritance
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


        

        
