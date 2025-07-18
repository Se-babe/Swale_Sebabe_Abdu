# Exercise 3: Sets

# 1. Use set() constructor to create a set of 3 favorite beverages
beverages = set(["Coffee", "Tea", "Juice"])
print("1. Beverages set:", beverages)

# 2. Add 2 more items to the beverages set
beverages.add("Water")
beverages.add("Soda")
print("2. Updated beverages set:", beverages)

# 3. Check if "microwave" is present in mySet
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("3. Is 'microwave' in mySet?", "microwave" in mySet)

# 4. Remove "kettle" from the set
mySet.discard("kettle")  # Use discard to avoid error if item not found
print("4. After removing 'kettle':", mySet)

# 5. Loop through the set
print("5. Looping through mySet:")
for item in mySet:
    print(" -", item)

# 6. Add elements from a list to a set
mySet2 = {"notebook", "pen", "eraser", "ruler"}
myList = ["marker", "sharpener"]
mySet2.update(myList)
print("6. Set after adding list elements:", mySet2)

# 7. Join two sets: one with ages, another with first names
ages = {21, 22, 23}
first_names = {"Swale", "Abdu", "John"}
joined_set = ages.union(first_names)
print("7. Joined set (ages + names):", joined_set)
