import random
"""
Assignment: Homework 2, Exercise 4.1
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: This program plays a simple number guessing game
"""


def main():
    # generate random target number
    target = random.randint(1, 20)

    # welcome msg
    print("I am thinking of a number between 1 and 20. You have 10 tries.")

    # actual gameplay
    for guess in range(10):
        answer = int(input(f"You have {10-guess} Guesses left.\nTake a Guess: "))

        # if they guessed the correct number print and end game
        if answer == target:
            print(f"Good job! You guessed my number in {guess+1} guesses!")
            return

        # if they wrong tell them where the guess is at
        print(f"Your guess is too {'low' if answer<target else 'high'}.")

    # Wow. You lost...
    print(f"Sorry, the number I was thinking of was {target}")

if __name__ == '__main__':
    main()