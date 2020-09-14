import random
"""
Assignment: Homework 2, Exercise 4.2
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: Expands on part 1 by adding variable range bounds
"""


def main():
    # generate random target number
    lower_bound = random.randint(1, 100)
    # give a little space between bounds so its not like guess between 2 and 3. Also not impossible (1, 40000)
    upper_bound = random.randint(lower_bound+20, lower_bound+120)
    target = random.randint(lower_bound, upper_bound)

    # welcome msg
    print(f"I am thinking of a number between {lower_bound} and {upper_bound}. You have 10 tries.")

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