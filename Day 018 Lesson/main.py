# from module import * - this will import everything
# import module as mos - this will create an alias you can use
from turtle import Turtle, Screen, colormode
from random import choice, randint
import colorgram

#######################################################################################################################
# timmy = Turtle()
# colors = ["aquamarine", "bisque", "blue", "BlueViolet", "CadetBlue", "chartreuse", "chocolate", "coral",
#           "CornflowerBlue", "cyan", "DarkGoldenrod1", "DarkGreen", "DarkOrchid", "DarkSeaGreen", "DarkSlateGray",
#           "DeepSkyBlue", "DodgerBlue", "firebrick", "gold", "indianred", "lawngreen", "lavender", "LightSlateBlue",
#           "LimeGreen", "OliveDrab", "purple", "RoyalBlue", "violet"]
# direction = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
# colormode(255)
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b
#######################################################################################################################
# # Draw a square
# for _ in range(4):
#     timmy.forward(200)
#     timmy.right(90)
#
# timmy.reset()
#
# # Dashed line
# for _ in range(20):
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)
#     timmy.pd()
#
# timmy.reset()
#
# sides = [3, 4, 5, 6, 7, 8, 9, 10]
# timmy.pensize(10)
# for item in sides:
#     col = choice(colors)
#     for _ in range(item):
#         timmy.pencolor(col)
#         timmy.forward(100)
#         timmy.right(360/item)
#
#
# def random_walk():
#     col = choice(colors)
#     turn = choice(direction)
#     timmy.pencolor(col)
#     timmy.forward(30)
#     timmy.setheading(turn)
#
#
# for step in range(200):
#     random_walk()


# def random_walk():
#     col = (random_color())
#     turn = choice(direction)
#     timmy.pencolor(col)
#     timmy.forward(30)
#     timmy.setheading(turn)
#
#
# for step in range(200):
#     random_walk()

# Making a spirograph
# timmy = Turtle()
#
# direction = [0, 90, 180, 270]
# # timmy.pensize(10)
# timmy.speed("fastest")
# colormode(255)
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)
#
#
# def draw_spirograph(gap_size):
#     for _ in range(int(360 / gap_size)):
#         timmy.pencolor(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap_size)
#
#
# draw_spirograph(3)

timmy = Turtle()

direction = [0, 90, 180, 270]
timmy.speed("fastest")
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

timmy.dot(20)







screen = Screen()
screen.exitonclick()
