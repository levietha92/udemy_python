import turtle as t

STEPS = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.pos = []
        self.create_snake()
        self.move()
        self.forward()
        self.backward()
        self.turn_left()
        self.turn_right()
    
    # def create_game(self):
    #     screen = t.Screen()
    #     screen.screensize(600,600)
    #     screen.bgcolor("black")
    #     screen.title("Welcome to Snake Game")
    #     screen.tracer()
    #     screen.listen()
    
    def create_snake(self, snake_length=3):
        for index in range(0,snake_length):
            pos_unit = -index * STEPS
            self.pos.append(pos_unit)
            
            square = t.Turtle(shape="square")
            square.penup()
            square.color("white")
            square.setx(self.pos[index])
            square.sety(0)
            square.speed(0)
            self.snake.append(square)

    def move(self):
        for index in range(len(self.snake)-1,0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)

    def forward(self):
        self.move()
        self.snake[0].forward(STEPS)

    def backward(self):
        self.move()
        self.snake[0].backward(STEPS)

    def turn_left(self):
        self.move()
        self.snake[0].left(90)
        self.snake[0].forward(STEPS)   

    def turn_right(self):
        self.move()
        self.snake[0].right(90)
        self.snake[0].forward(STEPS)  