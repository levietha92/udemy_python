import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

screen = t.Screen()
screen.screensize(3000,500)
tim.shape("turtle")
tim.color("purple")
for i in range(15):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()
  
screen.exitonclick()
