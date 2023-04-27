from turtle import Turtle
import random


COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'green']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class Cars:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(310, random_y)
            self.all_cars.append(car)

    def cars_running(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
