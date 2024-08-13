import pandas as pd
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from player import Player

# Create the Map in screen
image = "blank_states_img.gif"
screen = Screen()
screen.title("US STATES GAME")
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

# Generate player
player = Player()

# Generate scoreboard
scoreboard = ScoreBoard()

data = pd.read_csv('50_states.csv')
data['state_lower'] = data.state.str.lower()

game_is_on = True
answered_state = []

while game_is_on:
    # Getting the coordinate of the answered state
    user_answer = screen.textinput(title="",prompt="Name a US State").lower()
    ## If wrong state
    if user_answer not in data.state_lower.to_list():
        player.wrong_answer()
    ## If correct state
    else:
        state_x = int(data[data.state_lower == user_answer].x.iloc[0])
        state_y = int(data[data.state_lower == user_answer].y.iloc[0])
        print(state_x, state_y)
        answered_state.append(user_answer)
        scoreboard.add_score()
        scoreboard.show_score()

        # With given coordinate, identify on picture
        state_received = Player(state_x, state_y)
        state_received.correct_answer(user_answer.capitalize())
        
    # If enter a state that is already entered before (NOT WORK YET)
    if user_answer in answered_state and user_answer != answered_state[-1]:
        player.duplicate_answer()

    # Timer count down
    

