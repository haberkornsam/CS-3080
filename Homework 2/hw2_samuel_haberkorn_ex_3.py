"""
Assignment: Homework 2, Exercise 3
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: This program does list manipulation
"""

def main():
    # step 1, list
    items = ["Wallet", "Phone", "Keys"]
    # Step 1b, print
    print(f"Items: {items}")

    # step 2, sort and print
    items.sort()
    print(f"Sorted Items: {items}")

    # step 3, print first item
    print(f"First Item: {items[0]}")

    # step 4, print all but first
    print(f"All Items but the first: {items[1:]}")

    # step 5, print the last item
    print(f"Last Item: {items[-1]}")

    # step 6, print index of "Keys"
    print(f'Index of "Keys": {items.index("Keys")}')

    # step 7, Append tablet and print
    items.append("Tablet")
    print(f"Appended List: {items}")

    # step 8, Insert "Mask" at pos 2
    items.insert(2, "Mask")
    print(f"List with insert at pos 2: {items}")

    # step 9, remove "Phone" from list
    items.remove("Phone")
    print(f"List with no Phone: {items}")

    # step 10, reverse the list and print
    items.reverse()
    print(f"Reversed list: {items}")

    # step 11, print list in a friendly way
    print(f"Well printed list: {strList(items)}")


def strList(start_list: list) -> str:
    # There are three different cases with lists in the english language.
    # 1) 1 Element. Not really a list tbh
    # 2) 2 Elements. Includes "and" but no comma
    # 3) 3+ Elements. Includes "and" and commas comma

    if len(start_list) > 2:
        return ", ".join(cast_lists_to_str(start_list[:-1])) + f", and {start_list[-1]}"  # Yes we use oxford commas
    elif len(start_list) == 2:
        return f"{start_list[0]} and {start_list[1]}"
    elif len(start_list) == 1:
        return start_list[0]


# This function handles the instances where the list is not strings because .join() will not cast unfortunately

def cast_lists_to_str(items: list) -> str:
    for item in items:
        yield str(item)


if __name__ == '__main__':
    main()
