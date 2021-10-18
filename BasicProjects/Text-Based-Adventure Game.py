# This is a simple math based text-math adventure game
# It takes you on a math adventure

# Idea is simple, you need to solve 10 different math problems to save a princess from an evil arts student (No hate for
# arts students)
import sys


def run_():
    """ Runs the Save the Princess From an Evil Arts Student"""
    print("Welcome adventurer! \n A difficult task lies a head of you")
    print("An evil arts student has captured princess Leia and is keeping here in the darkest of dungeons")
    print("There are 3 doors gates you need to breach in order to rescue the beautiful princess")
    print("But not be fooled, these gates are sealed by magical spells....Very powerful spells")
    print("Even bravest have fallen to their death trying to unlock these doors")
    print("But I sense that you are different, adventurer. I sense wisdom, courage and knowledge." )
    print('Care to play the game of fate and rescue Princess Leia from this evil?')

    answer = input("Type Yes to play, and No to exit the game  ")

    if answer == "Yes" or  answer == "YES":
        print("Then let the adventure begin")
    else:
        sys.exit("Well, I have judged you wrongly. Bye!")

    print("Let's begin. I'm teleporting you to your first door...")
    print("#########################################################")
    print("A door appears. Its as normal as the doors can be. Wooden with a soft wooden door knob")
    print("You approach the door and place your hand on the door knob twisting it gently ")
    print("BAM! Light and darkness blend in a blink of a moment. You close your eyes from the fear of the unknown")
    print("And then you smell it.... a putrid smell of bad eggs and a loud hoarse voice saying")
    print("Hello stranger...I see yeeer comeee to yeeer death I seeee.. num num..")
    print("Says an ugly troll with a crooked nose, snot pouring from his oddly large nose holes")
    print("Tasty tasty...lookaa heerrre fresh meat fresh meat for my soup")
    print('But asss theeeezz damn rulezzz state...anybodi..even munches like yeer get a fayre trial by a problem.. ')
    print("So heeree it goes...the toughest of them all...")
    print("What is the sum of the exponents of the primes in the prime factorization of 210?")

    answer = input("Please input an integer answer: ")

    if int(answer) == 4:
        print("Yeeeer ..... correct. Ah.. no fresh meat for my soup..pass pass to save your princess")
        print( "Congratulations! You move on to the next door. You teleport to the next room")
    else:
        print("Unfortunately, you were captured by troll. Skinned alive, boiled in a soup, and eaten with")
        print("with a side of bread and cheese")
        sys.exit("Maybe next time! Bye!")
    print("#########################################################")

    print("""You have been teleported to the next door. It stands right in front of you, white as snow. Beside it lies a golden stone.""")

    answer = input("Would you like to pick it up? Type \"Yes\", otherwise type \"No\" ")
    stone = 0

    if answer == "Yes":
        print("You are stupid fool!! Muahahaha...(An artsy voice in the background)")
        print("You pick up the stone and place it in your pocket")
        stone = 1
    else:
        print(""" You ignore the stone and move towards the door """)

    print("""You approach the door. A sign appears in front of you. It states the following:
        Which of the following numbers is a perfect square? 
        A : 14!15!/2 
        B : 15!16!/2
        C : 16!17!/2
        D : 18!19!/2
        """)
    answer = input("Type in your answer. Choose one letter from the choices above: ")

    if answer == "D" or answer == "d":
        print("The door suddenly opens before you and you walk through it")

    else:
        sys.exit("""Without any notice, a huge boulder drops from the above squishing you into a pile of goo.
                    Maybe next time it will work out!""")

    print("As you walk through the door, you see a cage. In the cage, there is Princess Leia chained to the wall")
    print("In front of cage, an ugly, deformed arts student pops out")
    print(""" With a screeching voice it states ... Impossible! Those doors were impenetrable!
              But it does not matter... You won't be able to answer the last problem. Every one who tried 
              have failed """)
    print("So here is a question: Is the Riemann Hypothesis true?")

    if stone == 1:
        print("""Here are your options: \n
                 A: Yes \n
                 B: No  \n
                 C: Throw the stone at the dumb arts student""")
        answer = input("Please input one of the letters above: ")

        if answer == "C":
            print("""Congradulations! You picked the right choice. You threw the stone successfully at the arts student 
                     Knocking him out. You picked up his keys, freed Leia and lived happily ever after""")
            quit()
        else:
            print("You fool! This question has no answer. Now, I'll torture you forever")
            sys.exit("Unfortunately, you weren't able to free Leia. Now, you are going to have to listen to"
                     " an arts student babbling about political scinces, philosophy and other crap forever")

    else:
        print("""Here are your options: \n
                         A: Yes \n
                         B: No  """)
        answer = input("Please input one of the letters above: ")

        print("You fool! This question has no answer. Now, I'll torture you forever")
        sys.exit("Unfortunately, you weren't able to free Leia. Now, you are going to have to listen to"
                 " an arts student babbling about political scinces, philosophy and other crap forever")

run_()