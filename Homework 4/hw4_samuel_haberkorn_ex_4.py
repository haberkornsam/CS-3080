import re

"""
Assignment: Homework 4, Exercise 4
Name: Samuel Haberkorn
Date: October 22, 2020
Description: This program tests a password for it's strength. A strong password is at
least 8 characters long and has at least 1 uppercase, 1 lowercase, and 1 number
"""

# gets user input
password = input("Please enter a password to be tested: ")

# list of regexes
regexes = [
    re.compile(r'.{8,}'),  # length
    re.compile(r"[a-z]"),  # lowercase
    re.compile(r"[A-Z]"),  # uppercase
    re.compile(r"[0-9]")  # digits
]

strength = "strong"  # every pw starts as strong until a regex fails

# loop over the regexes and check if the password contains the pattern. if it doesn't weak pw and quit
for regex in regexes:
    if regex.search(password) is None:
        strength = "weak"
        break

print(f"This is a {strength} password.")
