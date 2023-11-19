from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.text = 1
        self.penup()
        self.goto(-200, 260)
        self.color("black")
        self.hideturtle()

    def show_level(self):
        self.write(f"Level:  {self.text}", align="center", font=FONT)

    def change_level(self):
        self.text += 1
        self.clear()
        self.show_level()
