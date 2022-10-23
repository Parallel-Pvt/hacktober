import random

while(True):
    b=int(input('Press 1 to continue \nPress 2 to exit\n'))
    if(b==2):
        break
    player1 = input("Select Rock, Paper, or Scissor :").lower()
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Player 2 selected: ", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won")
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Won")