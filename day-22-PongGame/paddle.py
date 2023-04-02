from turtle import Turtle

UP = 90
Down = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.penup()
        self.goto(position)

    def up(self):
        self.setpos(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
