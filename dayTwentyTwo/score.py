from turtle import Turtle

FONT = ("Courier", 14, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.text = ""
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(self.l_score, font=FONT)
        self.goto(100, 270)
        self.write(self.r_score, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, message):
        self.goto(0, 0)
        self.text = "GAME OVER\n"
        self.color("yellow")
        self.write(self.text + message, align="center", move=True, font=("Courier", 40, "bold"))
