"""
Assignment: Homework 3, Exercise 1
Name: Samuel Haberkorn
Date: Sept 28, 2020
Description: This program prints the character values from a list in a pretty way
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def main():
        #iterate over the rows and then join them together
        for line in grid:
                print("".join(line))

if __name__ == '__main__':
    main()