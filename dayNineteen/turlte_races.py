import random
import turtle
from turtle import Turtle, Screen

fig = Turtle()

turtle.colormode(255)


def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move_forw():
    fig.fd(10)


def move_backw():
    fig.bk(10)


def move_left():
    fig.lt(10)


def move_right():
    fig.rt(10)


def hilo(a, b, c):
    if c < b:
        b, c = c, b
    if b < a:
        a, b = b, a
    if c < b:
        b, c = c, b
    return a + c


def complement(color):
    r, g, b = color
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))


col = pick_color()
screen = Screen()
screen.onkeypress(move_forw, "Up")
screen.onkeypress(move_backw, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.listen()
fig.pencolor(complement(col))
screen.bgcolor(pick_color())
screen.exitonclick()
