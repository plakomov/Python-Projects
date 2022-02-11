# This is a beginner project of a rock, paper and scissors game
# Rules: 2 players only game
#        Rock beats Scissors, Scissors beat Paper and Paper beats Rock
#        Player who reaches 3 wins first wins the game



def rock_paper_scissors():
    """Runs the Rock Paper Scissors Game"""

    player_1_name = input("Please Input Player 1 Name: ")
    player_2_name = input("Please Input Player 2 Name: ")

    pl1_wins = 0
    pl2_wins = 0

    print("Choose R for Rock, S for Scissors and P for Paper")

    while pl1_wins < 3 and pl2_wins < 3:
        choice_1 = input("Make a choice {}, choose your weapon: ".format(player_1_name))
        choice_2 = input("Make a choice {}, choose your weapon: ".format(player_2_name))
        if outcome(choice_1, choice_2) == -1:
            print("Try again, invalid input")
        elif outcome(choice_1, choice_2) == 1:
            print("{} wins this round".format(player_1_name))
            pl1_wins += 1
        elif outcome(choice_1, choice_2) == 2:
            print("{} wins this round".format(player_2_name))
            pl2_wins += 1
        else:
            print("Its a tie this round, try again")
    if pl1_wins == 3:
        print("{} wins the game".format(player_1_name))
    else:
        print("{} wins the game".format(player_2_name))

def outcome(ch1, ch2):
    let = ["R", "P", "S"]
    if ch1 not in let or ch2 not in let:
        return -1
    if ch1 == "R":
        if ch2 == "R": return 0
        elif ch2 == "P": return 2
        else: return 1
    elif ch1 == "P":
        if ch2 == "P": return 0
        elif ch2 == "S": return 2
        else: return 1
    else:
        if ch2 == "S": return 0
        elif ch2 == "R": return 2
        else: return 1


rock_paper_scissors()
