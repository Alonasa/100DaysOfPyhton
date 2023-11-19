import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()
s = Scoreboard()
c = CarManager()
s.show_level()
screen.listen()
screen.onkey(p.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter = 0

    while counter < 1:
        if p.ycor() == 290:
            s.change_level()
        counter += 1
