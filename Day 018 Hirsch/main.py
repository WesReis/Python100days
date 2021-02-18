# import colorgram

# colors = colorgram.extract("hirst.jpg", 15)
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     hirst_colors.append((red, green, blue))
# print(hirst_colors)

from turtle import Turtle, colormode, Screen
from random import choice

hirst_colors = [(25, 102, 187), (236, 143, 83), (187, 43, 87), (249, 223, 82), (246, 75, 41), (4, 180, 221),
                (224, 75, 118), (186, 11, 33), (143, 75, 48), (237, 120, 166), (107, 184, 232), (24, 139, 84)]
timmy = Turtle()
timmy.speed("fastest")
colormode(255)
timmy.pu()
timmy.hideturtle()

space = 50
x = -300
y = -300
timmy.setpos(x, y)

for rol in range(10):
    for col in range(10):
        timmy.dot(20, choice(hirst_colors))
        x += space
        timmy.setpos(x, y)
    y += space
    x = -300
    timmy.setpos(x, y)

screen = Screen()
screen.exitonclick()
