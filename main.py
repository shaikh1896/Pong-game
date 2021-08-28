from turtle import Screen,Turtle
from ball import  Ball
import time
from paddle import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

li = [0.1,0.09,0.07,0.05,0.03,0.01,0.009,0.007,0.005,0.003,0.001]
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # DETECT COLLISION with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect miss with r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect miss with l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()








screen.exitonclick()