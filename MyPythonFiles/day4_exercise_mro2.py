class Admin:
    def role(self):
        print("Handles administration")

class Doctor:
    def role(self):
        print("Treats patients")

class Director(Admin, Doctor):
    pass

d = Director()
d.role()  # Output: Handles administration
print(Director.__mro__)
