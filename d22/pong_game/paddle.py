from turtle import Turtle, Screen

MOVE_DISTANCE = 15
SCREEN_SIZE = 1000
HALF_SIZE = SCREEN_SIZE / 2
GAME_ON = True
UP = 90

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = []
        self.create_paddle(side='left')
        self.head = self.paddle[0]

    def create_paddle(self, side):
        for ycor in [-MOVE_DISTANCE, 0, MOVE_DISTANCE]:
            square = Turtle(shape="square")
            square.penup()
            square.color("white")
            square.speed(0)
            if side == 'left':
                square.goto(-HALF_SIZE+20,ycor)
            else:
                square.goto(HALF_SIZE-20,ycor)
            self.paddle.append(square)
    
    # def move(self):
    #     for index in range(len(self.paddle)-1,0, -1):
    #         new_x = self.paddle[index - 1].xcor()
    #         new_y = self.paddle[index - 1].MOVE_DISTANCE()
    #         self.paddle[index].goto(new_x, new_y)
    #     self.head.setheading(UP)
    #     self.head.forward(MOVE_DISTANCE)
