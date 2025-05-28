# Polymorphism with Inheritance Example

# Superclass
class Bird:
    def fly(self):
        print("Birds fly in the sky")

# Derived class 1
class Eagle(Bird):
    def fly(self):
        print("Eagle soars high")

# Derived class 2
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flaps its wings swiftly")

# Polymorphic function
def flight_test(bird):
    bird.fly()

# Create objects
eagle1 = Eagle()
sparrow1 = Sparrow()

# Call the flight test method with different objects
flight_test(eagle1)    # Output: Eagle soars high
flight_test(sparrow1)  # Output: Sparrow flaps its wings swiftly
