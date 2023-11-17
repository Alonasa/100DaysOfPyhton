# from main_screen import Paddle
from turtle import Screen
from main_screen import MiddleLine
from paddle import Paddle

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
dashed = MiddleLine(HEIGHT).draw_dashed()
paddl1 = Paddle(WIDTH / 2 - 30, HEIGHT)
paddl2 = Paddle(-WIDTH / 2 + 30, HEIGHT)
current_paddle = paddl1

screen.listen()
screen.onkey(current_paddle.move_up, "w")
screen.onkey(current_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
