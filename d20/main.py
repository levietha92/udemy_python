"""
step 1: create a snake body
step 2: move the snake?
step 3: control the snake using keyboard input
step 4: create food
step 5: score tracking when snake eats food
step 6: game over conditions - hitting the wall or eat its tail
"""
from snake import Snake
from turtle import Screen

# step 1
snake = Snake()

screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer()
screen.listen()


# step 3
# snake.move()

screen.onkeypress(fun=snake.forward, key="Right")
screen.onkeypress(fun=snake.backward, key="Left")
screen.onkeypress(fun=snake.turn_left, key="Up")
screen.onkeypress(fun=snake.turn_right, key="Down")

# step 4


screen.exitonclick()
