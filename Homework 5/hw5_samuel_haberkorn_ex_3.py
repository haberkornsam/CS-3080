"""
Assignment: Homework 5, Exercise 3
Name: Samuel Haberkorn
Date: November 2, 2020
Description: This program mimics the builtin range function but with generator instead of a list
"""

def genrange(stop, start = 0, step = 1):
    i = start
    while i<stop:
        yield i
        i += step


# Test to check if the output is the same
for i in range(10, 20, 2):
    print(f"range: {i}")

for i in genrange(20, 10, 2):
    print(f"gen: {i}")
