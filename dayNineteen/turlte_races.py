import random
import turtle
from turtle import Turtle, Screen


def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = Screen()
turtle.colormode(255)
WIDTH = 500
HEIGHT = 400
screen.setup(WIDTH, HEIGHT)
screen.textinput("Make your bet!!!", "Who will win?")


def move_forw():
    value = random.randint(0, 100)
    fig.fd(value)


y = [-100, -70, -40, -10, 20, 50, 70]

for turtles in range(0, 6):
    fig = Turtle()
    fig.shape("turtle")
    fig.color(pick_color())
    fig.penup()
    fig.goto(x=-240.0, y=y[turtles])
    fig.pendown()
    screen.onkeypress(move_forw, "Up")


def move_backw():
    fig.bk(10)


def move_left():
    fig.lt(10)


def move_right():
    fig.rt(10)


def clear():
    fig.clear()
    fig.home()
    fig.pendown()


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
screen.onkeypress(move_backw, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(clear, "c")
screen.listen()
screen.exitonclick()
