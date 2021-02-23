from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, paddle_color, position):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.position = position
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
