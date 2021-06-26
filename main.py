from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score

L_PAD = (-350, 0)
R_PAD = (350, 0)

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(height=600, width=800, startx=250, starty=10)

screen.tracer(0)
screen.listen()
game_is_on = True

r_paddle = Paddle(R_PAD)
l_paddle = Paddle(L_PAD)
ball_object = Ball()
score = Score()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

while game_is_on:

    sleep(ball_object.value)
    screen.update()
    ball_object.move()  # moving the ball

    # Bouncing the ball
    if ball_object.ycor() > 300 or ball_object.ycor() < -300:
        ball_object.bounce()

    # detect collision with up wall and down wall
    if ball_object.xcor() > 400 or ball_object.xcor() < -400:
        game_is_on = False
        print("Game over")

    # detect collision with the left paddle
    if ball_object.distance(l_paddle) < 50 and ball_object.xcor() < 380:
        ball_object.left_bounce()
        ball_object.speed_fast()

    # detect collision with right paddle
    if ball_object.distance(r_paddle) < 50 and ball_object.xcor() > -380:
        ball_object.right_bounce()
        ball_object.speed_fast()

    # detect miss of left paddle and right paddle
    if ball_object.xcor() > 380:
        score.r_score()
        ball_object.game_reset()
        ball_object.left_bounce()

    if ball_object.xcor() < -380:
        score.x_score()
        ball_object.game_reset()
        ball_object.right_bounce()

screen.exitonclick()
