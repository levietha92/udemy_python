import time
from turtle import Screen
from player import Player
from car_manager import *
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
car_list = []
game_is_on = True
loop = 0
#increasing level
level = 0
score = Scoreboard()

while game_is_on:
    time.sleep(0.03)
    screen.update()
    screen.onkey(fun=tim.go_forward, key="Up")
    # screen.onkey(fun=tim.go_backward, key="Down")
    loop += 1
    if loop % (6-level) == 0:
        i = CarManager()
        car_list.append(i)

    for car in car_list:
        car.move()
        if tim.distance(car) <= 15:
            screen._write((0,0), "GAME OVER", "center", "Arial", "red")
            game_is_on = False

    if tim.reach_finish_line():
        level +=1
        score.update_score()
        screen._write((0,0), f"You won! To level {level}", "center", "Arial", "white")
        tim.player_reset()
    
    
    
