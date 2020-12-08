import os
import shutil

"""
Assignment: Homework 7, Exercise 2
Name: Samuel Haberkorn
Date: December 3, 2020
Description: The program finds pdf files in the directory and copies them to a new directory called "new_dir"
"""

def main():
    # target dir for files to be copied to
    target_dir = "./new_dir/"
    # print a header
    print(f"Path{'      '*15}Size (Bytes)")

    #iterate through dir tree and every file
    for root, subs, files in os.walk("."):
        for file in files:
            # if the last 4 characters of file are .pdf
            if file[-4:] == ".pdf":
                # print the absolute fp and the size of the file
                print(os.path.abspath(f"{root}/{file}"), os.path.getsize(f"{root}/{file}"), sep="\t\t")

                # make the target dir if it doesn't already exist and copy the file there
                os.makedirs(os.path.dirname(target_dir), exist_ok=True)
                shutil.copy(f"{root}/{file}", f"{target_dir}{file}")


if __name__ == '__main__':
    main()