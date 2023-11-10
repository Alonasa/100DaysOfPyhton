from turtle import Turtle, Screen

turtle_char = Turtle()
turtle_char.shape("turtle")
turtle_char.color("green")


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


colors = ['purple', 'light blue', 'pink', 'light green', 'violet', 'yellow', 'orange']


def fig(angles, color):
    count = 0
    angle = 360 / angles
    while count < angles:
        count += 1
        turtle_char.color(colors[color])
        turtle_char.backward(90)
        turtle_char.left(angle)


def shell():
    idx = 0
    for item in range(3, 10):
        fig(item, idx)
        idx += 1


shell()

screen = Screen()
