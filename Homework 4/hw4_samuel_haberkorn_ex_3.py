import pyperclip
import re

"""
Assignment: Homework 4, Exercise 3
Name: Samuel Haberkorn
Date: October 22, 2020
Description: Regex to match email addresses and phone numbers in the clipboard. Places them back into the clipboard
in CSV format
"""
regex = re.compile(
    r"""
    (?:(?:\+1(?:-|\b))? #Hanldes US Country code. It is optional and has a separate of whitespace or -
    (?:\d{10}| #simpliest case. Just 10 digits
    \(?[0-9]{3}\)?(?:-|\b|\.) #Handles area codes. May or may not have parenthesis. Separator of -, . or space
    \d{3}(?:-|\.)\d{4}) #easy end of number seperator of dash or .
    (?: ext?\.? \d+|\b|\.)) #handles extensions with ex. ex ext. ext as options
    | #Email Part
    (?:(?:[a-zA-Z0-9!#$%&'*+\-\/=?^_`{|}~.]+)@ #Local Name
    (?:[a-zA-Z0-9\.\-]*)\. #Domain Name
    (?:[a-zA-Z]{2,3})) #URL Extension
    """, re.X)

# take the output of a findall and place back in the clipboard with commas separating entries
pyperclip.copy(", ".join(regex.findall(pyperclip.paste())))
