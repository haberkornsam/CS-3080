import pprint

"""
Assignment: Homework 3, Exercise 2
Name: Samuel Haberkorn
Date: Sept 28, 2020
Description: This program counts the instances of each letter in a string, then prints it
"""

def main(string):
    letter_count = {}

    #iterate over range of capital letters
    #provide a count and add that to the dict
    for char in range(ord('A'), ord('Z')+1):
        letter_count[chr(char)] = string.upper().count(chr(char))

    pprint.pprint(letter_count)





if __name__ == '__main__':
    main("The quick brown fox jumps over the lazy dog")