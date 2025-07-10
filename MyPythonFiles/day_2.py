#control structures in python
# # 2. Comparison Operators: == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)
# # 3. Logical Operators: and, or, not
# # 4. Assignment Operators: = (assign), += (add and assign), -= (subtract and assign), *= (multiply and assign), /= (divide and assign)
# # 5. Bitwise Operators: & (bitwise AND), | (bitwise OR), ^ (bitwise XOR), ~ (bitwise NOT), << (left shift), >> (right shift)
# # Example:
# equals a == b
#not equal a != b
#greater than a > b
#less than a < b
#greater than or equal to a >= b
#less than or equal to a <= b
   
   
   #if statements ,# if statements are used to execute a block of code based on a condition. The syntax is as follows:
# if condition:
#     # Code to execute if the condition is true
# else:
#     # Code to execute if the condition is false

# Example:
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#
# Output: You are an adult.


#Nested if statements
# You can nest if statements to check multiple conditions. The syntax is as follows:
# if condition1:
#     if condition2:
#         # Code to execute if both conditions are true
#     else:
#         # Code to execute if condition1 is true but condition2 is false
# else:
#     # Code to execute if condition1 is false
# Example:
age = 20
if age >= 18:
    if age >= 21:
        print("You are eligible to drink alcohol.")
    else:
        print("You are not eligible to drink alcohol.")
else:
    print("You are a minor.")
    
    
    # loops (for and while loops    )
# Loops are used to execute a block of code repeatedly. Python has two main types of loops: for loops and while loops.
# 1. For Loop: Used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
# Syntax:
# for variable in sequence:
#     # Code to execute for each item in the sequence
# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

## 2. While Loop: Used to execute a block of code as long as a condition is true.
# Syntax:
# while condition:
#     # Code to execute while the condition is true
# Example:
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4
## break and continue statements
# The break statement is used to exit a loop prematurely, while the continue statement is used to
# skip the current iteration and move to the next one.
count = 1
while count <= 5:
    if count == 3:
        break
    print(count)
    count += 1
    
    #continue example
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
    
    #example  Guessing Game
     #in the example the user has to guess a number between 1 and 10. The loop continues until the user guesses the correct number.
import random
secret_number = random.randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print("Congratulations! You've guessed the number.")

#the lecturer talked of jupyter notebook and how it is used to run python code
 #python datab types
# # 2. While Loop: Used to execute a block of code as long as a condition is true.
# # Syntax:
# # while condition:
# #     # Code to execute while the condition is true
  #lists 
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# # Output:

# dictionary
 #it is used to store ordered data  changeably
 
dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dict)
# # You can access values using their keys.
print(dict["key1"])  # Output: value1


#using a pop to remove a string in python
dict.pop("key2")  # Removes the key-value pair with key "key2"
print(dict)  # Output: {'key1': 'value1', 'key3': 'value3'}

 