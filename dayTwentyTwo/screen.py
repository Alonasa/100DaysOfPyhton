from turtle import Screen, Turtle

screen = Screen()
line = Turtle()
HEIGHT = 600
WIDTH = 800
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

border_h = int(HEIGHT / 2)


def draw_dotted():
    line.hideturtle()
    line.goto(0, border_h)
    line.color("white")
    line.lt(270)
    for i in range(0, border_h - 10, 10):
        line.penup()
        line.forward(10)
        line.pendown()
        line.forward(10)


draw_dotted()

screen.exitonclick()
