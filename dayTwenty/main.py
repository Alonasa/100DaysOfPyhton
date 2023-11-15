from turtle import Screen, Turtle
import random, time
from snake import Snake

screen = Screen()
WIDTH = 1000
HEIGHT = 600
pos_x = int(WIDTH / 2 - 5)
pos_y = int(HEIGHT / 2 - 5)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

dot = Turtle("square")
dot.shapesize(0.5, 0.5)
dot.color("white")
dot.penup()
dot.goto(x=50.0, y=0.0)

new_snake = Snake()

no_wall = True
while no_wall:
    screen.update()
    time.sleep(0.5)

    new_snake.move()


def get_dot_coordinates():
    x = random.randint(-pos_x, pos_x)
    y = random.randint(-pos_y, pos_y)

    return x, y


dot.goto(get_dot_coordinates())

screen.exitonclick()
