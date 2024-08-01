"""
step 1: create a snake body
step 2: move the snake?
step 3: control the snake using keyboard input
step 4: create food, detect food collision
step 5: score tracking when snake eats food
step 6: game over conditions - hitting the wall or eat its tail
"""
from snake import *
import turtle as t
import random
import time


# step 1 - create screen
screen = t.Screen()
screen.screensize(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
print(food.xcor,food.ycor)
screen.listen()

is_game_on = True

# step 2 + 3
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkeypress(fun=snake.right, key="Right")
    screen.onkeypress(fun=snake.left, key="Left")
    screen.onkeypress(fun=snake.up, key="Up")
    screen.onkeypress(fun=snake.down, key="Down")

# step 4


screen.exitonclick()
