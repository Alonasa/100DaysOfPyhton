from turtle import Screen, Turtle
import random

screen = Screen()
WIDTH = 1000
HEIGHT = 600
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Turtle()
snake.shape("square")
snake.shapesize(0.2, 0.8)
snake.color("white")

dot = Turtle()
dot.shape("square")
dot.shapesize(0.2, 0.2)
dot.color("white")
dot.penup()
dot.goto(x=50.0, y=0.0)


def get_dot_coordinates():
    pos_x = int(WIDTH / 2 - 5)
    pos_y = int(HEIGHT / 2 - 5)
    x = random.randint(-pos_x, pos_x)
    y = random.randint(-pos_y, pos_y)

    return x, y


dot.goto(get_dot_coordinates())

screen.exitonclick()
