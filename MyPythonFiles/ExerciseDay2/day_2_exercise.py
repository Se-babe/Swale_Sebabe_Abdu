#grade basic using if statements ,elif statements, and else statements mark 80 grade A
mark = 80
if mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
else:
    print("Grade: D")



#create a list of cars and print each car in the list using a loop
cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]
for car in cars:
    print(car)
    
    
    #crate an ATM withdraw program use if else statements to check account balance before allowing withdrawal
account_balance = 1000  # Example account balance
withdrawal_amount = 200  # Example withdrawal amount
if withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful! New balance: ${account_balance}")
else:
    print("Insufficient funds.")

