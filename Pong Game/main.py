import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Creating screen/court
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

# Create paddles
scoreboard.update_score()
r_paddle = Paddle(paddle_color="blue", position=(350, 0))
l_paddle = Paddle(paddle_color="red", position=(-350, 0))
ball = Ball()

# Moving paddles
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# Playing game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # Detect collision with horizontal walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.wall_bounce()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_ball()
        r_paddle.goto(r_paddle.position)
        l_paddle.goto(l_paddle.position)

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_ball()
        r_paddle.goto(r_paddle.position)
        l_paddle.goto(l_paddle.position)


screen.exitonclick()
