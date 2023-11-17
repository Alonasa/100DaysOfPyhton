# from main_screen import Paddle
from turtle import Screen
from main_screen import MiddleLine
from paddle import Paddle
from ball import Ball
import time
from score import Score

HEIGHT = 600
WIDTH = 800
MAX_SCORE = 20

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
score = Score()


def move_current_paddle_up():
    current_paddle.move_up()


def move_current_paddle_down():
    current_paddle.move_down()


screen.listen()
screen.onkey(move_current_paddle_up, "w")
screen.onkey(move_current_paddle_down, "s")

game_is_on = True
score.update_scoreboard()

while game_is_on:
    screen.update()
    SPEED = 0.01
    ball.move()

    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(current_paddle) < 30 and ball.xcor() > 320 or ball.distance(
            current_paddle) < 30 and ball.xcor() < -320:
        current_paddle = change_paddle()
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score > MAX_SCORE or score.r_score > MAX_SCORE:
        ball.reset_position()
        score.game_over("Left side\nplayer loose!") if score.l_score < score.r_score else score.game_over(
            "Right side\nplayer loose!")

screen.exitonclick()
