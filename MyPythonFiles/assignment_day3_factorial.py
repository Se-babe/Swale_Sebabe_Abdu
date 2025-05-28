#factorial of five using lambda function
from functools import reduce
factorial = lambda n:reduce(lambda x,y:x * y,
range(1,n+1))
print(factorial(5))
