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
bet = int(screen.textinput("Make your bet!!!", "Who will win?"))


def move_forw():
    fig.fd(10)


y = [-100, -70, -40, -10, 20, 50, 70]

turtle_list = []

for turtles in range(0, 6):
    colour = pick_color()
    fig = Turtle()
    fig.shape("turtle")
    fig.color(colour)
    fig.penup()
    fig.goto(x=-240.0, y=y[turtles])
    fig.pendown()
    turtle_list.append(fig)

is_race = True
while is_race:
    for turtl in turtle_list:
        turtle_list[bet].pensize(5)
        value = random.randint(0, 15)
        turtl.fd(value)
        if turtl.xcor() > 230:
            idx = turtle_list.index(turtl)
            if bet == idx:
                print(f"The turtle {bet} are WON!")
            else:
                print(f"Sorry but your turtle {bet} lost and turtle {idx} Win")

            is_race = False


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
screen.listen()
screen.exitonclick()
