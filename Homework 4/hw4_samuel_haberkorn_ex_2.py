from math import sqrt, pow, pi
"""
Assignment: Homework 4, Exercise 2
Name: Samuel Haberkorn
Date: October 22, 2020
Description: This exercise makes 3 classes of difference shapes and inherits from one to the next.
Each class contains methods to find the perimeter, area, and diagonal. At the end we find the perimeter
of a circle who's radius is half the diagonal of a rectangle with sides 20 and 10
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_diagonal(self):
        return sqrt(pow(self.length, 2) + pow(self.width, 2))


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius * self.radius)

    def get_circumference(self):
        return 2 * pi * self.radius

    def get_diameter(self):
        return 2 * self.radius


rec = Rectangle(20, 10)
circle = Circle(rec.get_diagonal() / 2)

print(f"The Perimeter of the circle is {circle.get_circumference() :.2f}")
