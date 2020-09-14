"""
Assignment: Homework 2, Exercise 2
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: This program adds error handling to the first exercise
"""


def collatz(number: int) -> int:
    # figure out what the next number should be depending on even/odd
    next_num = number // 2 if number % 2 == 0 else (3 * number) + 1
    print(next_num)
    return next_num


def main():
    # add a default starting value to make my linter happy :)
    starting = 1

    # keep asking the user until they input an integer.
    while True:
        try:
            starting = int(input("Please enter an integer: "))
            break
        except ValueError:
            continue

    # Until the final number is 1 (the end goal) keep repeating the pattern
    # This would be a fun function to call recursively
    while starting != 1:
        starting = collatz(starting)


if __name__ == '__main__':
    main()
