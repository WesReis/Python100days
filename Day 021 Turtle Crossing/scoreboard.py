from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=-150, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
