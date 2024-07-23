import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.colormode(255) #RGB, tuples

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)

walk = [0,1]
tim.shape("turtle")

screen = t.Screen()
screen.screensize(3000,3000)
movements = random.randint(30,200)
x = 0

tim.speed(0)
while x in range(movements):
  direction = random.choice(walk)
  steps = random.randint(10,50)
  # tim.color(random.choice(colours))
  tim.color(random_color())
  tim.pensize(5)
  angle = random.randint(30,120)
  
  if direction == 0:
    tim.left(angle)
  else:
    tim.right(angle)  
  tim.forward(steps)
  x += 1
  
screen.exitonclick()