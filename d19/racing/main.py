import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

colors = ['red','blue','purple','pink','green','black']
pos_y = [0,-60,-40,-20,40,20]
turtle_list = []

winner = []
winning_mark = screen.window_width()/2 - 20
winning_turtle = ""

def init():
    global turtle_list
    for index in range(0,6):
        color_str = colors[index]
        y = int(pos_y[index])
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.color(color_str)
        new_turtle.penup()
        new_turtle.goto(-winning_mark,y)
        new_turtle.speed(0)
        turtle_list.append(new_turtle)
    return turtle_list

def race():
    global turtle_list, winning_turtle, winning_mark, winner
    count = len(turtle_list)
    for _ in range(0,count):
        turtle = random.choice(turtle_list)
        if turtle.xcor() >= winning_mark:
            winning_turtle = turtle.pencolor()
            winner.append(winning_turtle)
        else:
            turtle.forward(random.randint(0,10))

def game_end():
    global winner
    if len(winner) != 0:
        return True
    else:
        return False
    

user_bet = screen.textinput(title="Bet on your turtle", prompt="Enter a color: ")
turtle_list = init()


while not game_end():
    race()

if game_end():
    print(f"{winner[0]} is the winner")
    if user_bet == winner[0]:
        print("You won the bet!")
    else:
        print("You lost")

screen.exitonclick()

# res = {colors[i]: pos_y[i] for i in range(len(colors))}

# for index in res:
#     color_str = str(index)
#     y = int(res[index])
#     index = t.Turtle(shape="turtle")
#     index.color(color_str)
#     index.penup()
#     index.goto(-240,y)
#     index.speed(random.randrange(-10,10))
#     screen.listen()
#     screen.onkey(fun=race,key="space")