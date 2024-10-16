from scoreboardcross import Scoreboardcross
from turtle import Screen
import time
from car_manager import CarManager
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
score = Scoreboardcross()
score.hideturtle()
screen.listen()
screen.onkey(turtle.go_up, "Up")


game_is_on = True
while game_is_on:
    score.update()
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    for acar in car.newcar:
      if acar.distance(turtle) < 20:
        game_is_on = False

    if turtle.ycor() > 280:
        score.level += 1
        score.update()
        turtle.go_to_start()
        car.increase_speed()


score.game_over()



screen.exitonclick()