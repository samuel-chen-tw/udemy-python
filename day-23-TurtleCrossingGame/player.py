from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Pink")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.go_back()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

