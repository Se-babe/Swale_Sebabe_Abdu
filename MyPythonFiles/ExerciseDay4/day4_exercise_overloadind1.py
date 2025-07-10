#method overriding method overloading MRO method resolution order two real world examples
from functools import singledispatchmethod

class Calculator:
    @singledispatchmethod
    def calculate(self, value):
        raise NotImplementedError("Unsupported type")

    @calculate.register
    def _(self, value: int):
        print(f"Handling integer: {value * 2}")

    @calculate.register
    def _(self, value: str):
        print(f"Handling string: {value.upper()}")

calc = Calculator()
calc.calculate(10)       # Output: Handling integer: 20
calc.calculate("engine") # Output: Handling string: ENGINE
