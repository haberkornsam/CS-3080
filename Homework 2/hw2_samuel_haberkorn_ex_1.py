"""
Assignment: Homework 2, Exercise 1
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: This program performs and prints a collatz sequence based on a used inputted number
"""


def collatz(number: int) -> int:
    next_num = number // 2 if number % 2 == 0 else (3*number)+1
    print(next_num)
    return next_num


def main():
    starting = int(input("Please enter an integer: "))

    while starting != 1:
        starting = collatz(starting)


if __name__ == '__main__':
    main()
