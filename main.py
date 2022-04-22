from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
scoreboard = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.move_up, "o")
screen.onkey(r_paddle.move_down, "l")
screen.onkey(l_paddle.move_up, "q")
screen.onkey(l_paddle.move_down, "a")

game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
        ball.speed_bump()

    #Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        ball.speed_bump()

    #Detect Misses w/ Right Paddle
    if ball.xcor() > 380:
        ball.direction = -1
        ball.reset()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    #Detect Misses with Left Paddle
    if ball.xcor() < -380:
        ball.direction = 1
        ball.reset()
        scoreboard.r_point()
        scoreboard.update_scoreboard()



screen.listen()
screen.exitonclick()
