# In this project, I'm going to create a program that simulates dice rolling. It will allow the user to input their
# own probabilities fpr the 6 different states or use the "Unbiased" probability transition matrix

import numpy as np

def main():
    """Runs the dice simulation"""
    print("""Hello! Welcome to the Dice Rolling Simulator! In this simulator, you will be able to roll the dice and 
      even input your own probabilities for the dice making it a biased dice""")

    answer = input("Would you like to use the Unbiased Die? Type Yes or No: ")

    if answer == "Yes":
        roll = True
        while roll:
            print("Let's roll the dice")
            outcome = np.random.randint(1, 6, 1)
            print("The dice rolled {}".format(outcome))
            answer = input("Would you like to roll the dice one more time? Type Yes or No: ")
            if answer == "No":
                roll = False
    else:
        probs = []
        i = 1
        while i <= 6:
            num = input("Please input a positive integer that you would associate with number {}: ".format(i))
            probs.append(int(num))
            i += 1
        tpm = [num/sum(probs) for num in probs]
        roll = True
        while roll:
            print("Let's roll the biased dice")
            outcome = np.random.choice([1, 2, 3, 4, 5, 6], p=tpm)
            print("The dice rolled {}".format(outcome))
            answer = input("Would you like to roll the dice one more time? Type Yes or No: ")
            if answer == "No":
                roll = False
    return print("Thank you for using the Dice Simulator!")




main()