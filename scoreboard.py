from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_left}   {self.score_right}", align=ALIGNMENT, font=FONT)