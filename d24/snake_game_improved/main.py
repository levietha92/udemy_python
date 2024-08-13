"""
step 1: create screen, snake
step 2: move the snake?
step 3: control the snake using keyboard input
step 4: create food, detect food collision
step 5: score tracking when snake eats food
step 6: game over conditions - hitting the wall or eat its tail
"""
from snake import *
from food import Food
from scoreboard import ScoreBoard
import random
import time
import numpy as np


# step 1 - create screen
screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
# screen.screensize(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

# step 2 + 3
while GAME_ON == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkeypress(fun=snake.right, key="Right")
    screen.onkeypress(fun=snake.left, key="Left")
    screen.onkeypress(fun=snake.up, key="Up")
    screen.onkeypress(fun=snake.down, key="Down")

# step 4 + 5: catch food and scoring
    while snake.head.distance(food) <= DISTANCE:
        snake.add_length()
        scoreboard.add_score()
        food.refresh()

# step 6: collision with wall
    if abs(snake.head.xcor()) >= HALF_SIZE or abs(snake.head.ycor()) >= HALF_SIZE:
        scoreboard.reset()
        snake.reset()
        snake = Snake()
        snake.move()

# step 6: collision with itself:
    for square in snake.snake[1:snake.len+1]:
        if snake.head.distance(square) < 10:
            print("uhoh")
            scoreboard.reset()
            snake.reset()
            snake = Snake()
            snake.move()

screen.exitonclick()
