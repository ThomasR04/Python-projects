from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.newcar = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def gen_random_colour(self):
        random_colour = random.choice(COLORS)
        self.color(random_colour)

    def get_random_position(self):
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)

    def generate_car(self):
        new_car = CarManager()
        random_number = random.randint(1, 6)
        if random_number == 1:
          new_car.shape("square")
          new_car.gen_random_colour()
          new_car.shapesize(1, 2)
          new_car.penup()
          new_car.get_random_position()
          self.newcar.append(new_car)


    def move_cars(self):
        for cars in self.newcar:
            cars.backward(self.car_speed)

    def increase_speed(self):
            self.car_speed += MOVE_INCREMENT


