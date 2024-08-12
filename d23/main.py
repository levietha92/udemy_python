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

while game_is_on:
    
    time.sleep(0.03)
    screen.update()
    screen.onkey(fun=tim.go_forward, key="Up")
    # screen.onkey(fun=tim.go_backward, key="Down")
    loop += 1
    if loop % 4 == 0:
        i = CarManager()
        car_list.append(i)

    for car in car_list:
        car.move()
        if tim.distance(car) <= 15:
            screen._write((0,0), "GAME OVER", "center", "Arial", "red")
            game_is_on = False

    if tim.reach_finish_line():
        screen._write((0,0), "You won!", "center", "Arial", "white")
        game_is_on = False
    
    
    
