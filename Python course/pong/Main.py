from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
game_ball = Ball()
Scores = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    game_ball.speed(2)
    screen.update()
    game_ball.move()
    time.sleep(game_ball.movespeed)

    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.boumce_y()

    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    if  game_ball.xcor() > 380:
        Scores.update_scoreboard_l()
        Scores.update()
        game_ball.reset_position()
        game_ball.bounce_x()
        time.sleep(2)

    if game_ball.xcor() < -380:
        Scores.update_scoreboard_r()
        Scores.update()
        game_ball.reset_position()
        game_ball.bounce_x()
        time.sleep(2)







screen.exitonclick()