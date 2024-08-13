import pandas as pd
from turtle import Turtle, Screen

FONT = ("Arial",12,"normal")

screen = Screen()
screen.title("US STATES GAME")

# Create the Map in screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
scoreboard = Turtle()


data = pd.read_csv('50_states.csv')
data['state_lower'] = data.state.str.lower()

game_is_on = True
score = 0
answered_state = []

while game_is_on:
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(350,350)
    scoreboard.write(f"Score: {score}", False, align="right", font=("Arial",30,"normal"))
    # Getting the coordinate of the answered state
    user_answer = screen.textinput(title="",prompt="Name a US State").lower()
    ## If wrong state
    if user_answer not in data.state_lower.to_list():
        turtle.write("It doesn't exist, Try again", False, align="center", font=FONT)
    ## If correct state
    else:
        state_x = int(data[data.state_lower == user_answer].x.iloc[0])
        state_y = int(data[data.state_lower == user_answer].y.iloc[0])
        print(state_x, state_y)
        answered_state.append(user_answer)
        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}", False, align="right", font=("Arial",30,"normal"))

    # With given coordinate, identify on picture
    state_received = Turtle()
    state_received.hideturtle()
    state_received.penup()
    state_received.goto(state_x, state_y)
    state_received.write(user_answer.capitalize(), False, align="center", font=FONT)
    
    # If enter a state that is already entered
    # if user_answer in answered_state:
        # turtle.write("You already entered that", False, align="center", font=FONT)

    # Timer count down
    

