#method overriding method overloading MRO method resolution order two real world examples
class Vehicle:
    def start_engine(self):
        print("Starting vehicle engine...")

class Car(Vehicle):
    def start_engine(self):  # Overrides the parent method
        print("Starting car engine with a key...")

car = Car()
car.start_engine()  # Output: Starting car engine with a key...
