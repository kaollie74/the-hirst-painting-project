import colorgram as cg
import turtle as t
import random

""" Extract colors from image """
# color_list = cg.extract("hirst-image.jpg", 2 ** 32)
# color_palette = []
#
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r, g, b))
#
# print(color_palette)
# print(len(color_palette))

t.colormode(255)  # allows us to user rgb instead of string color
turtle = t.Turtle()  # instantiate Turtle object
turtle.speed("fastest")
turtle.hideturtle()
colors = [(249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130),
          (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111),
          (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148),
          (122, 190, 160),
          (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202),
          (238, 64, 34), (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42), (9, 87, 103),
          (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]

""" Move to starting point """
turtle.setheading(225)
turtle.penup()
turtle.fd(300)
turtle.setheading(0)


def move_dots():
    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.fd(50)


def go_left():
    turtle.setheading(90)  # turn north
    turtle.fd(50)
    turtle.setheading(180)  # turn east
    turtle.fd(500)
    turtle.setheading(0)  # turn west


for _ in range(10):
    move_dots()
    go_left()

screen = t.Screen()
screen.exitonclick()
