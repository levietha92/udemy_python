"""
step 1: create a snake body
step 2: move the snake?
step 3: control the snake using keyboard input
step 4: create food
step 5: score tracking when snake eats food
step 6: game over conditions - hitting the wall or eat its tail
"""

import turtle as t
import time

#step 1
snake = []
pos = [0,-20,-40]
# snake.shapesize(stretch_len=3) # a whole body approach, but can't find doc on moving first block independent from the rest
for index in range(0,3):
    square = t.Turtle(shape="square")
    square.penup()
    square.color("white")
    square.setx(pos[index])
    square.sety(0)
    square.speed(0)
    snake.append(square)


screen = t.Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer()


#step 2
steps = 20 

def move():
    for index in range(len(snake)-1,0, -1):
        new_x = snake[index - 1].xcor()
        new_y = snake[index - 1].ycor()
        snake[index].goto(new_x, new_y)

def forward():
    move()
    snake[0].forward(steps)

def backward():
    move()
    snake[0].backward(steps)

def turn_left():
    move()
    snake[0].left(90)
    snake[0].forward(steps)   

def turn_right():
    move()
    snake[0].right(90)
    snake[0].forward(steps)        

def clear():
    snake[0].clear()
    screen.resetscreen()

screen.listen()

# step 3
screen.onkeypress(fun=forward, key="Right")
screen.onkeypress(fun=backward, key="Left")
screen.onkeypress(fun=turn_left, key="Up")
screen.onkeypress(fun=turn_right, key="Down")

# step 4


screen.exitonclick()
