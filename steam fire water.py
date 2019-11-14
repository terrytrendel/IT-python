import random

player_score = 0
computer_score = 0
print("============================")
print("   STEAM, FIRE, WATER       ")
print("      By.Terry Trendel      ")
print("      and Adam Bulk         ")
print("============================")

t = ["", "Steam", "Fire", "Water"]

print("We are going to play Steam, Fire, Water. The first to win two out of three rounds is the winner.")
input("")
while player_score < 2:
    print(f"{player_score} - {computer_score}")
    print("")
    if computer_score == 2:
        print("You lose")
        break
    print("1. Water")
    print("2. Fire")
    print("3. Steam")
    player_choice = int(input("What do you choose? "))
    computer_choice = random.randint(1, 3)
    if player_choice == computer_choice:
        print("tie")
    elif player_choice == 1:
        if computer_choice == 2:
            print(f"you lose! {t[computer_choice]} covers {t[player_choice]}")
            computer_score = computer_score + 1
        else:
            print(f"you win! {t[player_choice]} covers {t[computer_choice]}")
            player_score = player_score + 1
    elif player_choice == 2:
        if computer_choice == 3:
            print(f"you lose! {t[computer_choice]} covers {t[player_choice]}")
            computer_score = computer_score + 1
        else:
            print(f"you win! {t[player_choice]} covers {t[computer_choice]}")
            player_score = player_score + 1
    elif player_choice == 3:
        if computer_choice == 1:
            print(f"you lose! {t[computer_choice]} covers {t[player_choice]}")
            computer_score = computer_score + 1
        else:
            print(f"you win! {t[player_choice]} covers {t[computer_choice]}")
            player_score = player_score + 1






if player_score == 2:
    print("You win")