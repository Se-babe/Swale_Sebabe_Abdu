'''write  a program to handle errors the program should ask for two numbers using input and then divides them use an infinite loop to keep asking until a valid input is provide'''
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print(" Invalid input! Please enter numbers only.")
    except ZeroDivisionError:
        print(" Cannot divide by zero. Try again.")
    else:
        print(f"✅ Result: {num1} / {num2} = {result}")
        break  # Exit loop after a successful operation
