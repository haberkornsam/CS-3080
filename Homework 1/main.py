import random
'''
Homework 1
Samuel Haberkorn
September 8, 2020
Security program. When everything is completed successfully a secret message is printed
'''


def main():
    print("Welcome to my super secure program!")
    success = False

    while not success:

        #step one. Enter a number
        print("Enter a number between 24 and 26")
        number = int(input())
        if not (26 >= number >= 24):
            continue

        #step two. Perform a calculation
        #You get three guesses
        num1 = random.randint(4, 46)
        num2 = random.randint(4, 46)
        print(f"That is correct! Now enter the product of {num1} and {num2}. You have 3 guesses!")

        for attempt in range(3):
            if int(input()) == num1*num2:
                success = True
                break
            elif attempt != 2:
                print("Incorrect, try again")
            else:
                print("Oof that's not good")

        if not success:
            success = False
            continue

        success = False

        #Step three. A question to make you think

        print("You are doing good. How many days are in a year? Accurate to two decimal places")

        number = float(input())

        if number != 365.24:
            continue

        #Step 4. Enter a multiple value
        print("Almost done! Here is an easy one. \n Enter a multiple of 27")

        if int(input())%27 != 0:
            continue


        #step 5. Provide details of the user
        print("Enter the name of the person's information you would like to access!")

        string = input()

        if string.upper() != "SAM":
            continue

        #step 6. Make this frustratingly long

        for num in range(3):
            print(f"Please enter 34*{num}")
            if int(input()) != num*34:
                success = True
                break

        if success:
            success = False
            continue

        success = False

        #step 7. Satisfy project requirements for len and string. The int() is to make sure it is a number

        print("Please enter a number that is 6 digits long")
        if len(str(int(input()))) != 6:
            continue

        #step 8
        print("Please enter the number zero")
        if int(input()):
            continue

        #step 9
        print("enter the solution to this problem: 5+32-1)")

        if int(input()) != 5+32-1:
            continue

        print("Congratulations! Here is a super secret piece of information ;) ")
        print("****************************")
        print("Email: haberkornsam@gmail.com")
        print("****************************")
        print("Thanks for playing!!")
        success = True









if __name__ == '__main__':
    main()