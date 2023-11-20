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
    c.create_car()
    c.move_cars()

    if p.ycor() == 290:
        s.change_level()
        p.starting_position()

    for car in c.cars:
        if car.distance(p) < 20:
            c.game_over()
            game_is_on = False

screen.exitonclick()
