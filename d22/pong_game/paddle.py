from turtle import Turtle

SCREEN_SIZE = 600
HALF_SIZE = SCREEN_SIZE/2
MOVE_DISTANCE = 50
PADDLE_DISTANCE = 50

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        # self.paddle = Turtle(shape='square')
        self.shape("square")
        # self.speed(0)
        self.side = side
        self.penup()
        self.color("white")
        self.shapesize(3,1)
        if self.side == "left":
            self.goto(-HALF_SIZE + 30,0)
        else:
            self.goto(HALF_SIZE - 30,0)

        self.up()
        self.down()            

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)