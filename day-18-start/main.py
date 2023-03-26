import random
from turtle import Turtle, Screen
import random as r

claire = Turtle()
claire.shape("turtle")
claire.color("pink")

screen = Screen()
screen.colormode(255)

# for _ in range(50):
#     claire.forward(10)
#     claire.penup()
#     claire.forward(10)

# for angle in range(3, 9):
#     color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
#     claire.pencolor(color)
#     for line in range(angle):
#         claire.forward(100)
#         claire.right(360/angle)

# DIRECTION = [0, 90, 180, 270]
# color = ['LightPink', 'LightSalmon', 'PeachPuff', 'Plum', 'PaleTurquoise', 'LightSteelBlue']
# claire.pensize(10)
# claire.speed(10)
#
#
# def direction():
#     return DIRECTION[r.randint(0, 3)]
#
#
# for _ in range(400):
#     claire.pencolor(random.choice(color))
#     claire.setheading(direction())
#     claire.fd(30)

color = ['LightPink', 'LightSalmon', 'PeachPuff', 'Plum', 'PaleTurquoise', 'LightSteelBlue']
claire.speed('fastest')
count = 0

for _ in range(count, 72):
    count += 5
    claire.pencolor(random.choice(color))
    claire.circle(100)
    claire.setheading(count)


screen.exitonclick()
