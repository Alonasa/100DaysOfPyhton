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
dashed = MiddleLine(HEIGHT).draw_dashed()
paddl1 = Paddle(WIDTH / 2 - 30)
paddl2 = Paddle(-WIDTH / 2 + 30)

screen.exitonclick()
