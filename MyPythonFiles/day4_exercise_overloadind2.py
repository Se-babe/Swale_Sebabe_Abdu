#method overriding method overloading MRO method resolution order two real world examples
class Report:
    def generate(self, patient=None):
        if patient:
            print(f"Generating report for {patient}")
        else:
            print("Generating general hospital report")

r = Report()
r.generate("John Doe")  # Output: Generating report for John Doe
r.generate()            # Output: Generating general hospital report
