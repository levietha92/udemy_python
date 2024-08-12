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
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    screen.onkey(fun=tim.go_forward, key="Up")
    screen.onkey(fun=tim.go_backward, key="Down")

    # print(time.clock_gettime)
    i = CarManager()
    car_list.append(i)

    for car in car_list:
        car.move()
        if tim.distance(car) <= 10:
            print("GAME OVER")
            game_is_on = False
            
    if tim.reach_finish_line():
        game_is_on = False
    
    
    
