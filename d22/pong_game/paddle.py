from turtle import Turtle

SCREEN_SIZE = 800
HALF_SIZE = SCREEN_SIZE/2
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.paddle = Turtle(shape='square')
        self.side = side
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(5,1)
        if self.side == "left":
            self.paddle.goto(-HALF_SIZE + 30,0)
        else:
            self.paddle.goto(HALF_SIZE - 30,0)

        self.up()
        self.down()            

    def up(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)