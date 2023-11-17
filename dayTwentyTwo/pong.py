# from main_screen import Paddle
from turtle import Screen
from main_screen import MiddleLine
from paddle import Paddle
from ball import Ball
import time

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
dashed = MiddleLine(HEIGHT).draw_dashed()
r_paddl = Paddle(WIDTH / 2 - 30, HEIGHT)
l_paddl = Paddle(-WIDTH / 2 + 30, HEIGHT)
current_paddle = r_paddl


def change_paddle():
    global current_paddle, r_paddl, l_paddl
    if current_paddle == r_paddl:
        current_paddle = l_paddl
    elif current_paddle == l_paddl:
        current_paddle = r_paddl
    return current_paddle


ball = Ball()
screen.listen()


def move_current_paddle_up():
    current_paddle.move_up()


def move_current_paddle_down():
    current_paddle.move_down()


screen.onkey(move_current_paddle_up, "w")
screen.onkey(move_current_paddle_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(current_paddle) < 30:
        ball.bounce_x()
        current_paddle = change_paddle()

screen.exitonclick()
