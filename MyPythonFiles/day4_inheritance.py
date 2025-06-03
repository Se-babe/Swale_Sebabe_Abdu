#demonstrate inheritance in python
# inheritance is a way to create a new class from an existing class
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
    def speak(self):
        print("Woof")
        super().speak()
