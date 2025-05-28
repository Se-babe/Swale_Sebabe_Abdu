class Electric:
    def power_source(self):
        print("Electric power")

class Diesel:
    def power_source(self):
        print("Diesel power")

class Hybrid(Electric, Diesel):
    pass

vehicle = Hybrid()
vehicle.power_source()  # Output: Electric power
print(Hybrid.__mro__)   # Shows the resolution order
