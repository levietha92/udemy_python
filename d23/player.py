from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_backward(self):
        self.backward(MOVE_DISTANCE)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:        
            return True
        else:
            return False

    def player_reset(self):
        self.goto(STARTING_POSITION)