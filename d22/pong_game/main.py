from paddle import *
# from pong import Pong
from scoreboard import ScoreBoard
import random
import time
import numpy as np


# step 1 - create screen
screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")


# scoreboard = ScoreBoard()
paddle = Paddle()
left_paddle = paddle.create_paddle(side='left')
right_paddle = paddle.create_paddle(side='right')


# pong = Pong()

# screen.listen()

