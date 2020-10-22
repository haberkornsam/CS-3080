import pyperclip
import sys

"""
Assignment: Homework 4, Exercise 1
Name: Samuel Haberkorn
Date: October 22, 2020
Description: This is a simple password manager that copies the password to the clipboard
"""


passwords = {
    "instagram": "password1",
    "facebook": "superSecurePassword",
    "canvas": "1s2d3f4g5",
    "email": "PieCookieCake",
    "steam": "SamsPassword",
}

if len(sys.argv) != 2:
    print(f"Invalid number of argument. Expected 1 found {len(sys.argv)-1}")
    exit(1)

try:
    pyperclip.copy(passwords[sys.argv[1].lower()])
    print("Password Copied!")
except KeyError:
    print("Account Not Found")
    exit(1)
