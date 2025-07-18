# Exercise 2: Tuples

# 1.	Consider the tuple below;
#x = (“samsung”, “iphone”, “tecno”, “redmi”)
	#Write a python program to output your favorite phone brand.

x = ("samsung", "iphone", "tecno", "redmi")
print("1. My favorite phone brand is:", x[0])  

# 2.Use negative indexing to print the 2nd last item in your tuple. 
print("2. 2nd last item:", x[-2])  # tecno

#3.	Using the phones list above, write a python program to update “iphone” to “itel”
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("3. After update:", x)

# 4.	Write a python program to add “Huawei” to your tuple.
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print("4. After adding Huawei:", x)

# 5.	Write a python program to loop through the tuple above.
print("5. Looping through tuple:")
for phone in x:
    print(" -", phone)

# 6.	Write a python program to remove/delete the first item in your tuple
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print("6. After removing first item:", x)

# 7.	Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Gulu", "Arua", "Mbarara", "Jinja"])
print("7. Cities in Uganda:", cities)

# 8.	Write a python program to unpack your tuple.
city1, city2, city3, city4, city5 = cities
print("8. Unpacked Cities:")
print(city1, city2, city3, city4, city5)

# 9.	Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("9. 2nd to 4th cities:", cities[1:4])

#10.	Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("Swale", "Abdu", "John")
second_names = ("Sebabe", "Kamulegeya", "Doe")
full_names = first_names + second_names
print("10. Joined names:", full_names)

# 11.	Create a tuple of colors and multiply it by 3.
colors = ("Red", "Green", "Blue")
colors_multiplied = colors * 3
print("11. Colors multiplied by 3:", colors_multiplied)

# 1.	Create a tuple of colors and multiply it by 3.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("12. Number of times 8 appears:", count_8)
