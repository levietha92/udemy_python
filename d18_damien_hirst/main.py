import turtle as t
import random

color_list = [(191, 143, 162), (153, 173, 199), (135, 74, 96), (171, 101, 125), (217, 198, 206), (65, 42, 48), (214, 177, 191), (182, 164, 148), (61, 48, 44), (107, 95, 69), (199, 203, 215), (79, 100, 116), (98, 46, 61), (212, 203, 198), (179, 187, 211), (39, 57, 46), (123, 145, 80), (79, 99, 79), (151, 169, 155), (47, 44, 67), (52, 49, 98), (76, 57, 55), (201, 208, 202), (204, 185, 183), (172, 104, 95), (200, 196, 168), (122, 122, 145), (48, 72, 58), (114, 143, 97), (71, 76, 40), (182, 197, 190), (173, 198, 207), (49, 73, 77), (111, 134, 142)]

timmy = t.Turtle()
timmy.speed(10)
screen = t.Screen()
screen.colormode(255)
timmy.hideturtle()

angle = 90
dot_size = 10
space = dot_size * 2
scale = 10


def draw_line(scale):
    for x in range(scale-1):
        timmy.dot(dot_size,random.choice(color_list))
        timmy.penup()
        timmy.forward(space)
        timmy.dot(dot_size,random.choice(color_list))
    
def transit(direction):
    if direction == "right":
        timmy.right(angle)
        timmy.penup()
        timmy.forward(space)
        timmy.right(angle)
    else:
        timmy.left(angle)
        timmy.penup()
        timmy.forward(space)
        timmy.left(angle)


def draw_two_lines(scale):
    draw_line(scale)
    transit("right")
    draw_line(scale)
    transit("left")

rounds = int(scale/2)

for _ in range(rounds):
    draw_two_lines(scale)

screen.exitonclick()
