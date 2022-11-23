from prac_09.car import Car
from random import randint as rn


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = rn(1, 100)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
