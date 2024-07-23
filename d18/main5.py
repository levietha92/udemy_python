import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

screen = t.Screen()
screen.screensize(3000,3000)

tilt = 5
radius = 50
movements = int(360/5)
tim.speed(0)

for _ in range(0,movements):
    tim.color(random_color())
    tim.circle(radius)
    tim.left(tilt)
    
    
screen.exitonclick()
