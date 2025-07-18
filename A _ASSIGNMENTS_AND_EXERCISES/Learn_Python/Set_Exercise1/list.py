
#1.	Create a list with 5 items (names of people) and write a python program to output the 2nd item.
people = ["Alice", "Brian", "Charles", "Diana", "Ethan"]
print("2nd item:", people[1])

#2.	Write a python program to change the value of the first item to a new value
people[0] = "Alex"
print("After changing first item:", people)

#3.	Write a python program to add a sixth item to the list
people.append("Faith")
print("After adding sixth item:", people)



#4.	Write a python program to add “Bathel” as the 3rd item in your list
people.insert(2, "Bathel")
print("After inserting Bathel as 3rd item:", people)

#5.	Write a python program to remove the 4th item from the list

people.pop(3)
print("After removing 4th item:", people)

#6.	Use negative indexing to print the last item in your list

print("Last item:", people[-1])

#7.	Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
items = ["Pen", "Pencil", "Eraser", "Sharpener", "Book", "Bag", "Ruler"]
print("3rd to 5th items:", items[2:5])

#8.	Write a list of countries and make a copy of it.
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "South Sudan"]
countries_copy = countries.copy()
print("Original:", countries)
print("Copy:", countries_copy)

#9.	Write a python program to loop through the list of countries
for country in countries:
    print("Country:", country)


#10.	Write a list of animal names and sort them in both descending and ascending order.

animals = ["Zebra", "Elephant", "Antelope", "Lion", "Cheetah"]
animals.sort()
print("Ascending:", animals)
animals.sort(reverse=True)
print("Descending:", animals)

#11.	Using the list above, write a python program to output only animal names with the letter ‘a’ in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animals with 'a':", animals_with_a)



#12.	Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["Swale", "Abdu", "John"]
second_names = ["Sebabe", "Kamulegeya", "Achol"]
full_names = first_names + second_names
print("Joined list:", full_names)
