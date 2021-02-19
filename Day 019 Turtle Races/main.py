from turtle import Turtle, Screen
from random import randint

# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.fd(10)
#
#
# screen.listen()
# # this is a higher order function, where a function calls another function
# screen.onkey(fun = move_forwards, key = "space")
# screen.exitonclick()
########################################################################################################################
# tim = Turtle()
# screen = Screen()
# screen.listen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_back():
#     tim.backward(10)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def anti_clockwise():
#     tim.left(10)
#
#
# def clear_screen():
#     tim.reset()
#
#
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_back, key="s")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=anti_clockwise, key="a")
# screen.onkey(fun=clear_screen, key="c")
# screen.exitonclick()
########################################################################################################################
# Turtle race
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_pos = -170
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 56
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 200:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"Your {winning_color} turtle won! 😁")
            else:
                print(f"{winning_color.title()} turtle won, your {user_bet} turtle lost! 😭")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()