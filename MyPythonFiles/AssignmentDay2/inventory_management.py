#create an inventory management system use loops to display or update a list of stock items
# Inventory list: each item is a dictionary
inventory = []

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    inventory.append({"name": name, "quantity": quantity, "price": price})
    print(f"{name} added to inventory.")

def update_item():
    display_inventory()
    item_index = int(input("Enter item number to update: ")) - 1
    if 0 <= item_index < len(inventory):
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_index]['quantity'] = new_quantity
        print("Item quantity updated.")
    else:
        print("Invalid item number.")

def remove_item():
    display_inventory()
    item_index = int(input("Enter item number to remove: ")) - 1
    if 0 <= item_index < len(inventory):
        removed = inventory.pop(item_index)
        print(f"{removed['name']} removed from inventory.")
    else:
        print("Invalid item number.")

# Main loop
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        display_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
