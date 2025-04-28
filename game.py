print(" \n 🎮 HELLO PLAYERS 🎮 \n",
      "Welcome to  Rock✊, Paper✋, Scissors✌️ game \n" )

print("RULE OF THE GAME: \n" \
"Please choose one between ; rock, paper, or scissors \n")

import getpass

p1_name = input("Player one enter you name please :")
player1 = getpass.getpass(f"Enter you choice {p1_name} :").lower()
print("Your choice was saved")

print("\n")

p2_name = input("Player two enter your name please :")
player2 = getpass.getpass(f"Enter your choice {p2_name} :").lower()
print("Your choice was saved")

valid_choices = ["rock", "paper", "scissors"]
if player1 not in valid_choices :
    print(f"{p1_name} you entered an invalid choice")

elif player2 not in valid_choices:
    print(f"{p2_name} you entered an invalid choice")
else:
    if player1 == player2 :

        print("\n\n")
        print ("It's a TIE for both of you")
        print("\n\n")

    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper") :
        
        print("\n\n")
        print(f"{p1_name} choose : {player1}")
        print(f"{p2_name} choose : {player2}")
        print("\n")
        print(f"🎉 The winner is {p1_name} 🎉 ")
        print("\n\n")
    else:
        print("\n\n")
        print(f"{p1_name} choose : {player1}")
        print(f"{p2_name} choose : {player2}")
        print("\n")
        print(f"🎉 The winner is {p2_name} 🎉")
        print("\n\n")