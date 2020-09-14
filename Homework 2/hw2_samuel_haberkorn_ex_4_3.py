import random
"""
Assignment: Homework 2, Exercise 4.3
Name: Samuel Haberkorn
Date: Sept 13, 2020
Description: Expands part 2 by making the computer play the game in a very unintelligent way
"""


def main():
    # generate random target number
    lower_bound = random.randint(1, 100)
    # give a little space between bounds so its not like guess between 2 and 3. Also not impossible (1, 40000)
    upper_bound = random.randint(lower_bound+20, lower_bound+120)
    target = random.randint(lower_bound, upper_bound)

    # welcome msg
    print(f"I am thinking of a number between {lower_bound} and {upper_bound}. You have 10 tries.")

    guesses = []
    for guess in range(10):
        print(f"You have {10 - guess} Guesses left.")


        # make sure we haven't guessed that number yet
        rand = None
        while rand is None or rand in guesses:
            rand = random.randint(lower_bound, upper_bound)
        guesses.append(rand)

        #play the game and if it is successful they quit
        if play(rand, target, lower_bound, upper_bound) == 1:
            print(f"Good job! You guessed my number in {guess + 1} guesses!")
            return

    #if we bad bad
    print(f"Sorry, the number I was thinking of was {target}")


def play(answer: int, target: int, lower: int, upper: int) -> int:
    # actual gameplay from previous exercise main
    print(f"Take a Guess: {answer}")

    # if they guessed the correct number print and end game
    if answer == target:
        return 1

    # if they wrong tell them where the guess is at
    print(f"Your guess is too {'low' if answer < target else 'high'}.")

    return 0

if __name__ == '__main__':
    main()