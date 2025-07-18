#exercise1
#write a function to get product of three values
def product_of_three(a, b, c):
    return a * b * c
# Test the function
result = product_of_three(2, 3, 4)
print("The product of 2, 3, and 4 is:", result)

#exercise2
#use return statement to  divide two numbers using a function
def divide_numbers(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
# Test the function
result = divide_numbers(10, 2)
print("The result of dividing 10 by 2 is:", result)
# Test with division by zero
result_zero = divide_numbers(10, 0)
