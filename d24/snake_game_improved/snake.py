from turtle import Turtle, Screen
import time
import random

DISTANCE = 15
SCREEN_SIZE = 600
HALF_SIZE = SCREEN_SIZE / 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
GAME_ON = True

class Snake:
    def __init__(self,snake_length=3):
        self.snake = []
        self.pos = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]
        self.len = snake_length

    def create_snake(self,snake_length=3):
        # pos = [0,-10,20]
        for index in range(0,snake_length):
            pos_unit = -index * DISTANCE
            self.pos.append(pos_unit)
            square = Turtle(shape="square")
            square.shapesize(0.85,0.85,1)
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
        self.head.forward(DISTANCE) #before it was glitchy without connection due to this inside the for loop

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

    def add_length(self):
        square = Turtle(shape="square")
        square.penup()
        square.shapesize(0.85,0.85,1)
        square.color("white")
        square.speed(0)
        square.goto(self.tail.xcor(), self.tail.ycor())
        self.snake.append(square)
        self.len += 1

