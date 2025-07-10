#find the factorial of a number 5 using a lambda function
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
result = factorial(5)
print("The factorial of 5 is:", result)
# This code defines a lambda function to calculate the factorial of a number.
# It uses recursion to compute the factorial, where the base case is when x is 0
# (factorial of 0 is 1), and for other values, it multiplies x by the factorial of (x - 1). 
# The result is then printed to the console.
# Note: This is a simple implementation and may not handle large numbers efficiently due to recursion depth
# limitations in Python. For larger numbers, consider using an iterative approach or the math library.
# which provides a built-in factorial function.
