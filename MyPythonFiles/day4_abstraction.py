# Abstraction Example in Python

from abc import ABC, abstractmethod  # Importing for abstraction

# Define abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # No implementation — abstract method

# Child class 1
class Car(Vehicle):
    def start(self):
        print("Car engine starts")

# Child class 2
class Bike(Vehicle):
    def start(self):
        print("Bike engine starts")

# Create objects of concrete subclasses
car1 = Car()
bike1 = Bike()

# Call their start methods
car1.start()   # Output: Car engine starts
bike1.start()  # Output: Bike engine starts
