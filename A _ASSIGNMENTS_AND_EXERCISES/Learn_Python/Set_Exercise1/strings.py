# Exercise 4: Strings

# 1. Declare two variables, an integer and a string, and concatenate
age = 25
message = "I am " + str(age) + " years old."
print("1.", message)

# 2. Remove spaces at the beginning, middle, and end
txt = "      Hello,       Uganda!       "
txt_no_spaces = txt.strip().replace("       ", " ")
print("2.", txt_no_spaces)

# 3. Convert the value of ‘txt’ to uppercase
print("3.", txt.upper())

# 4. Replace character ‘U’ with ‘V’
replaced_txt = txt.replace("U", "V")
print("4.", replaced_txt)

# 5. Return characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
substring = y[1:4]
print("5. Characters in 2nd, 3rd, and 4th position:", substring)

# 6. Correcting the string with double quotes inside
x = 'All "Data Scientists" are cool!'
print("6.", x)
