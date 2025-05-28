#method overriding method overloading MRO method resolution order two real world examples
class Staff:
    def duty(self):
        print("Performing general staff duty")

class Nurse(Staff):
    def duty(self):
        print("Providing medical care to patients")

n = Nurse()
n.duty()  # Output: Providing medical care to patients
