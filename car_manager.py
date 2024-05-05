from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SIZES = [2, 2, 3, 3, 2, 2]


class CarManager:
    def __init__(self):

        self.trafic_list = []
        self.move_speed = MOVE_INCREMENT

    def create_car(self, img):

        new_car = Turtle('square')
        new_car.shapesize(1, random.choice(SIZES))

        new_car.shape(img)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(1000, random.randint(0, 7) * 45 - 35)
        for car in self.trafic_list:
            if car.distance(new_car) == 0:
                new_car.goto(1100, random.randint(0, 7) * 45 - 35)

        self.trafic_list.append(new_car)

    def move(self, x):
        for car in self.trafic_list:
            car.bk(self.move_speed + x * 2)

    def fast_move(self):

        for car in self.trafic_list:
            car.bk(10 * self.move_speed)




