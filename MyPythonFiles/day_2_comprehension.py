#lists and dictionaries
# List comprehension
# list = [expression for item in iterable if condition]
# Example:
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16

#example2 list comprehension with condition
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4]

