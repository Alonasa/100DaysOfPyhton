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


screen = Screen()
