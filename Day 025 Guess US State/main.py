import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# This will print out the coordinates on the screen
# def get_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_coor)
# turtle.mainloop()

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                                    prompt="What's the state name?").title()
    # print(answer_state)
    if answer_state in states_list and answer_state not in states_guessed:
        states_guessed.append(answer_state)
        state = states[states.state == answer_state]
        xcoor = int(state.x)
        ycoor = int(state.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=xcoor, y=ycoor)
        t.write(answer_state)


# screen.exitonclick()
