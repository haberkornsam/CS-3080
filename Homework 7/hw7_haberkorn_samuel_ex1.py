import os
import re
import shutil

"""
Assignment: Homework 7, Exercise 1
Name: Samuel Haberkorn
Date: December 3, 2020
Description: The program converts date formats in file names within a directory. From mm-dd-yyyy to yyyy-mm-dd
"""

# All valid months. All valid days. Years from 1800 to 2000+
DATE_REGEX = r'(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])-[12][890][0-9]{2}'


def main():
    # walk the file tree iterating over all the files
    for root, dirs, files in os.walk("."):
        for file in files:
            # check if filename contains a date
            date = re.search(DATE_REGEX, file)
            if date is None:
                continue

            # take filename from begin to start of date. Add the year. Then the month and day. Add remaining filename
            new_name = f"{file[:date.start()]}{file[date.end() - 4:date.end()]}-{file[date.start():date.end() - 5]}{file[date.end():]}"
            # rename file using relative path names for subdirectories
            shutil.move(f"{root}/{file}", f"{root}/{new_name}")


if __name__ == '__main__':
    main()
