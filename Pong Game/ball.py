from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(x=new_x, y=new_y)

    def wall_bounce(self):
        self.y_change *= -1

    def paddle_bounce(self):
        self.x_change *= -1
        self.move_speed *= 0.9
    #
    # def speed_up(self):
    #     if self.x_change > 0:
    #         self.x_change += 1
    #     else:
    #         self.x_change -= 1
    #     if self.y_change > 0:
    #         self.y_change += 1
    #     else:
    #         self.y_change -= 1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()
