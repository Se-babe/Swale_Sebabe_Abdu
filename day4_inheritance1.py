#inheritance,super class,parent class
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat1 = Cat()
cat1.speak()
