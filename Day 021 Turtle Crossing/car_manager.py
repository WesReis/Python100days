from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.goto(x=300, y=randint(-250, 250))
            self.all_cars.append(new_car)

    def car_move(self):
        move_speed = self.car_speed
        for car in range(len(self.all_cars)-1):
            new_x = self.all_cars[car].xcor() - move_speed
            new_y = self.all_cars[car].ycor()
            self.all_cars[car].goto(x=new_x, y=new_y)

    def car_level_up(self):
        self.car_speed =+ MOVE_INCREMENT

