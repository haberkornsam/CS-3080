"""
Assignment: Homework 3, Exercise 3
Name: Samuel Haberkorn
Date: Sept 28, 2020
Description: This program manages an inventory system
"""

def print_inventory(inventory: dict):
    #print with a header
    print(f"{'Item': <16}Quantity")
    for key in inventory:
        print(f"{key: <16}{inventory[key]}")

def add_item(inventory: dict, item):
    #Quick way to increment if it exists. Note the zero increments to one when an item is added
    inventory[item] = inventory.get(item, 0)+1

def delete_item(inventory: dict, item):
    #Subtract one if there are 2 or more items, delete if there is 1 remaining
    if inventory.get(item, 0) > 1:
        inventory[item] -= 1
    else:
        inventory.pop(item)


def main():
    inventory = {
        "Hand Sanitizer": 10,
        "Soap": 6,
        "Kleenex": 22,
        "Lotion": 16,
        "Razors": 12,
    }

    print_inventory(inventory)
    print("\nAdding Advil and Lotion")
    print("-"*24)
    add_item(inventory, "Lotion")
    add_item(inventory, "Advil")
    print_inventory(inventory)

    print("\nDeleting Soap and Advil")
    print("-" * 24)
    delete_item(inventory, "Soap")
    delete_item(inventory, "Advil")
    print_inventory(inventory)

if __name__ == '__main__':
    main()