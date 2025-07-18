
# 1. Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("1. Shoe size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("2. Updated brand:", Shoes["brand"])

# 3. Add a new key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("3. Updated dictionary:", Shoes)

# 4. Return a list of all the keys
keys = list(Shoes.keys())
print("4. Keys in dictionary:", keys)

# 5. Return a list of all the values
values = list(Shoes.values())
print("5. Values in dictionary:", values)

# 6. Check if the key “size” exists
key_exists = "size" in Shoes
print("6. Is 'size' key present?", key_exists)

# 7. Loop through the dictionary
print("7. Looping through dictionary:")
for key, value in Shoes.items():
    print(f" - {key}: {value}")

# 8. Remove “color” from the dictionary
Shoes.pop("color", None)
print("8. Dictionary after removing 'color':", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("9. Dictionary after clearing:", Shoes)

# 10. Create and copy a new dictionary
Student = {
    "name": "Sebabe",
    "age": 22,
    "course": "Software Engineering"
}
Student_copy = Student.copy()
print("10. Original dictionary:", Student)
print("    Copied dictionary:", Student_copy)

# 11. Show nested dictionaries
School = {
    "Student1": {
        "name": "Ali",
        "age": 21
    },
    "Student2": {
        "name": "Zara",
        "age": 22
    }
}
print("11. Nested Dictionary:")
for student, info in School.items():
    print(f" - {student}: {info}")
