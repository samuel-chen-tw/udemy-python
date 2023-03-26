# import colorgram
#
# color_list = []
# pic_color = colorgram.extract('hirst-painting.png', 80)
# for index in range(30):
#     color_rgb = pic_color[index].rgb
#     color_r = color_rgb.r
#     color_g = color_rgb.g
#     color_b = color_rgb.b
#     color_list.append((color_r, color_g, color_b))
#
# print(color_list)
import random
import turtle as t

claire = t.Turtle()
screen = t.Screen()
t.colormode(255)
color_rgb_list = [(248, 245, 241), (248, 245, 247), (206, 154, 106), (237, 240, 243), (125, 146, 160), (65, 99, 114), (237, 243, 241), (165, 62, 47), (125, 173, 159), (117, 89, 105), (24, 38, 51), (239, 191, 134), (94, 110, 106), (65, 47, 22), (134, 138, 92), (213, 102, 87), (85, 164, 138), (155, 104, 117), (233, 165, 162), (170, 137, 141), (152, 37, 39), (33, 72, 79), (152, 38, 36), (229, 166, 169), (32, 65, 63), (118, 127, 141), (95, 141, 153), (36, 75, 73), (174, 202, 194), (62, 61, 70)]
color = ['LightPink', 'LightSalmon', 'PeachPuff', 'Plum', 'PaleTurquoise', 'LightSteelBlue']
claire.speed('fastest')
claire.penup()
claire.setheading(225)
claire.fd(325)
claire.setheading(0)
claire.hideturtle()


for index in range(1, 101):
    # claire.dot(20, random.choice(color_rgb_list))
    claire.dot(20, color[random.randint(0, 5)])
    claire.fd(1)
    if index % 10 == 0:
        claire.left(90)
        claire.fd(50)
        claire.left(90)
        claire.fd(460)
        claire.left(180)
    else:
        claire.fd(50)



screen.exitonclick()

