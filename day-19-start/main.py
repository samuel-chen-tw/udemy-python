from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x = -230
y = -100
is_race_on = False
all_turtles = []


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y + (turtle_index+1) * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lose... The {winner_color} turtle is the winner!")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)



screen.exitonclick()


# from turtle import Turtle, Screen
#
# claire = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     claire.forward(10)
#
#
# def move_backwards():
#     claire.backward(10)
#
#
# def counter_clockwise():
#     heading = claire.heading()
#     heading += 10
#     claire.setheading(heading)
#
#
# def clockwise():
#     heading = claire.heading()
#     heading -= 10
#     claire.setheading(heading)
#
#
# def clear_drawing():
#     claire.clear()
#     claire.penup()
#     claire.home()
#     claire.penup()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=counter_clockwise)
# screen.onkeypress(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_drawing)
# screen.exitonclick()


