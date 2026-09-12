"""
Hiding the implementation details of the class
only showing essential features to the user
"""


class Vehicle:
    def __init__(self):
        self.engine = False
        self.brake = False

    def start_engine(self):
        self.engine = True
        self.brake = True
        print("Engine started")


car1 = Vehicle()
car1.start_engine()

from abc import ABC, abstractmethod


class Gaadi(ABC):
    @abstractmethod
    def engine_start(self):
        pass


class Car(Vehicle):
    def engine_start(self):
        print("Car Started")


car = Car()
car.engine_start()
