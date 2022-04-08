import random


def get_number():

    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    return lower, upper


def guess_number(x):

    print("\nYou've only 3 guesses")

    # Initializing the number of guesses.
    count = 0
    tries = 3

    # for calculation of minimum number of guesses depends upon range
    while count < tries:
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ", count, " tries !!!")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses, shows this output.
    if count >= tries:
        print("\nThe number is %d !" % x)
        print("Better Luck Next time !!!")


lower, upper = get_number()
x = random.randint(lower, upper)
guess_number(x)
