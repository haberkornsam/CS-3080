"""
Assignment: Homework 5, Exercise 1
Name: Samuel Haberkorn
Date: November 2, 2020
Description: This program creates a reverse iterator that returns a list backwards
because iter(list.reverse()) is too much typing
"""

class ReverseIter:
    def __init__(self, my_list):
        self.list = my_list
        self.i = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 0:
            return self.list[self.i]

        raise StopIteration


it = ReverseIter([1,2,3,4])
for i in range(5):
    print(next(it))