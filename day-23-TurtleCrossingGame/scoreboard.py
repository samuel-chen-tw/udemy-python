from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_board()

    def add_level(self):
        self.level += 1

    def update_board(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

