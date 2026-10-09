import random

computer = random.choice(["rock", "paper", "scissors"])

player = input("Choose rock, paper, or scissors: ")

print("Computer chose:", computer)

if player == computer:
    print("Drow")

elif player == "rock" and computer == "scissors":
    print("You win")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

else:
    print("Computer wins")