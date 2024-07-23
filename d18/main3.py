import turtle as t
import random as random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

screen = t.Screen()
screen.screensize(3000, 3000)

tim.shape('turtle')
colors = ['red','blue']

for side in range(3,11):
  tim.color(random.choice(colors))
  for i in range(side):
    tim.forward(100)
    tim.right(360/side)
  
tim.showturtle()


screen.exitonclick()