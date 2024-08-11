from turtle import Screen, Turtle
from paddle import Paddle, SCREEN_SIZE
import time



# step 1 - create screen
screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")




left_paddle = Paddle("left")
right_paddle = Paddle("right")

screen.listen()

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="a")
screen.onkey(fun=right_paddle.up, key="o")
screen.onkey(fun=right_paddle.down, key="l")

screen.exitonclick()