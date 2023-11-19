import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
turtle_char = Turtle()
turtle_char.shape("arrow")
turtle_char.color("green")


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


def square():
    count = 0
    while count < 4:
        count += 1
        turtle_char.forward(100)
        turtle_char.left(90)


def dashed():
    count = 0
    while count < 10:
        count += 1
        turtle_char.forward(10)
        turtle_char.up()
        turtle_char.forward(5)
        turtle_char.down()


def fig(angles, color):
    count = 0
    angle = 360 / angles
    while count < angles:
        count += 1
        turtle_char.color(color)
        turtle_char.backward(90)
        turtle_char.left(angle)


def shell():
    for item in range(3, 10):
        color = get_color()
        fig(item, color)


def spirograph():
    deg = 6
    counter = 360 / deg

    while counter > 0:
        counter -= 1
        turtle_char.pencolor(get_color())
        turtle_char.circle(100)
        turtle_char.left(deg)


spirograph()

screen = Screen()
screen.exitonclick()
