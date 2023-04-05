from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars_list = []
        self.hideturtle()
        self.create_car()

    def create_car(self):
        number = random.randint(1, 6)
        if number == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(1, 2)
            new_car.goto(300, random.randint(-250, 250))
            self.cars_list.append(new_car)

    def cars_move(self):
        for car in self.cars_list:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT
