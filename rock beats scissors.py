import random

print("============================")
print("   ROCK, PAPER, SCISSORS    ")
print("      By.Terry Trendel      ")
print("      and Adam Bulk         ")
print("============================")

print("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner.")

player_choice = random.choice(1, 3)

print("SCORE: Player: {0} Computer:{0}")

print("1.Rock")
print("2.Paper")
print("3.Scissors")

player_choice = int(input("What is your choice? "))
if player_choice == 'rock' or 'paper' or 'scissors':
    if player_choice == 1:
        if Computer == 'Rock':
print("Tie Game")
    elif Computer == ("Paper"):
        print ("Computer Wins")
    else:
        print ("User Wins")
if player_choice == ("paper"):
    if Computer == "(Rock"):
        print ("User Wins")
    elif Computer == ("Paper"):
        print ("Tie Game")
    else:
        print ("Computer Wins")
if user == ("scissors"):
    if Computer == ("Rock"):
        print ("Computer Wins")
    elif Computer == ("Paper"):
        print ("YOU Win")
    else:
        print ("Tie Game")