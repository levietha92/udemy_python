#####Turtle Intro######

import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############



#screen setting
screen = t.Screen()
screen.screensize(2000,1500)


# create turtle
po = t.Turtle()
po.shape('turtle')
po.color('DarkTurquoise')
for i in range(1,5):
  po.right(90)
  po.forward(100)
  
po.showturtle()


screen.exitonclick()
