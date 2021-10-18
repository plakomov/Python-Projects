
# A program that randomly generates a number between the range specified [Int, Int]
# The program gives the user a clue about the number and for each wrong guess the points are reduced from the TOTAL
# points
# Clues can be anything we want them to be

import random

def number_guessing_game_():
    total_score = 10

    print("Welcome to the Number Guessing Game")
    a = input("Please the lower bound of your range: ")
    b = input("Please the upper bound of your range: ")

    while int(a) >= int(b):
        print("Invalid bounds\nPlease try again")
        a = input("Please the lower bound of your range: ")
        b = input("Please the upper bound of your range: ")

    print("Picking a random number between {} and {}".format(a, b))

    answer = random.randint(int(a), int(b))
    score = total_score

    print("Let's begin the guessing!")
    print("Current score: {} out of {} ".format(score, total_score))


    guess = input("Please input your guess: ")

    while int(guess) != answer and score != 0:
        print("Unfortunately, that is not the answer")
        print("Here is a hint: {} is multiple of your guess and the answer".format(int(guess)*answer))
        guess = input("Please input your new guess: ")
        score -= 1

    if score == 0:
        print("Unfortunately, you lost.")
        print("The answer was {}".format(answer))
        print("Your score is 0")
    else:
        print("Congratulations! Your score is {} out of {}".format(score, total_score))



number_guessing_game_()

