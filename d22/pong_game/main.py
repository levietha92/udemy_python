from turtle import Screen, Turtle
from paddle import *
from pong import Pong
from scoreboard import *
import time
import random



# step 1 - create screen
screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")
screen.mode("standard")
screen.tracer(0)

# step 2 - create paddles
left_paddle = Paddle("left")
right_paddle = Paddle("right")

left_score = ScoreBoard(-20,HALF_SIZE-40)
right_score = ScoreBoard(20,HALF_SIZE-40)

# step 3 - paddles move independently
screen.listen()
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="a")
screen.onkey(fun=right_paddle.up, key="o")
screen.onkey(fun=right_paddle.down, key="l")

# step 4 - create the pong
pong = Pong()

# the game
game_is_on = True
hit_paddle = False
left_strike = 0
right_strike = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong.move()
    print(f"Heading = {pong.heading()}, {pong.pos()}")
    
    # Collision with paddle --> bounce
    if pong.distance(right_paddle) <= PADDLE_DISTANCE and pong.xcor() > HALF_SIZE - PADDLE_DISTANCE:
        print("contact")
        pong.bounce_x()

    if pong.distance(left_paddle) <= PADDLE_DISTANCE and pong.xcor() > -HALF_SIZE + PADDLE_DISTANCE:
        print("contact")
        pong.bounce_x()

    # Collision with North and South walls --> bounce
    if abs(pong.ycor()) >= HALF_SIZE - 30:
        pong.bounce_y()
    
    # Collision with LEFT and RIGHT walls --> score for opponent
    if pong.xcor() >= HALF_SIZE - 15:
        left_score.add_score()
        right_strike += 1
        pong.reset()
    
    if pong.xcor() <= -HALF_SIZE + 15:
        right_score.add_score()
        left_strike += 1
        pong.reset()
    
    if right_strike == 3 or left_strike == 3:
        game_is_on = False
        pong.write("GAME OVER", False, align=ALIGN, font=(FONT, FONTSIZE +20, FONTTYPE))


    
screen.exitonclick()