import shelve, sys, pyperclip

"""
Assignment: Homework 6, Exercise 3
Name: Samuel Haberkorn
Date: November 11, 2020
Description: This program is a command line tool that holds multiple items in the clipboard.
"""

file = shelve.open("storage")


#Make sure the script is run with arguments
if len(sys.argv) == 1:
    print("Error: 1 argument expected. Found 0")
    exit(1)

#if the 1st arg is saved, make sure there is a key to save by. Then copy to clipboard
if sys.argv[1].lower() == 'save':
    if len(sys.argv) < 3:
        print("Error: 2 arguments expected. Found 1")
        exit(1)
    file[sys.argv[2]] = pyperclip.paste()
    print("Clipboard contents saved!")

#if the 1st arg is to list, print all the contents
elif sys.argv[1].lower() == 'list':
    print("Keywords")
    print("--------")
    print("\n".join(file.keys()))


#Extra!! Add functionality to remove a entry from storage.
elif sys.argv[1].lower() == 'delete':
    if len(sys.argv) < 3:
        print("Error: 2 arguments expected. Found 1")
        exit(1)
    if file.get(sys.argv[2]) is None:
        print("Error: Keyword Not Found")
        exit(1)

    file.pop(sys.argv[2])
    print("Item Removed!")


#if the 1st arg is none, check if its a key then copy the contents to clipboard
else:
    if file.get(sys.argv[1]) is None:
        print("Error: Keyword Not Found")
        exit(-1)
    pyperclip.copy(file[sys.argv[1]])
    print("Contents Copied!")

file.close()