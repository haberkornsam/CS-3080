from math import sqrt, pow
"""
Assignment: Homework 5, Exercise 2
Name: Samuel Haberkorn
Date: November 2, 2020
Description: This program prints the first n pythagorean triples. We were not told how to rank them 
(i.e. what number to sort by x, y, or z) I made the assumption that it was the first value (x).
"""

# integer function from class... Endless stream of ints
def integers():
    i=1
    while True:
        yield i
        i += 1

# Just iterates through the sequence n times
def take(n, seq):
    seq = iter(seq)
    results = []
    try:
        for i in range(n):
            results.append(next(seq))
    except StopIteration:
        pass
    return results



#actual logic stuff... create a nested for loop with an infite num of y values. that spawn x values up until the y value. Check if the sqrt of their squares is an int. if it is yield that value.
#This is sorted by x value
pyt = ((x, y, int(sqrt(pow(x, 2)+pow(y, 2)))) for y in integers() for x in range(1, y) if sqrt(pow(x, 2)+pow(y, 2)).is_integer())


print(take(11, pyt))