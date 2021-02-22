from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        rand_x = randint(-260, 260)
        rand_y = randint(-260, 200)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)


