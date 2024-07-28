from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

steps = 50

def move_forwards():
    tim.forward(steps)

def move_backwards():
    tim.backward(steps)

def move_clockwise():
    tim.circle(-steps)

def move_counter_clockwise():
    tim.circle(steps)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    screen.resetscreen()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
