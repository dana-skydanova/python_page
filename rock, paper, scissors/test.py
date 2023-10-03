import random

player = input("Select Rock, Paper, or Scissors: ").lower()
computer = random.choice(["Rock", "Paper", "Scissors"]).lower()
print("Computer selected: ", computer)

if player == "Scissors" and computer == "scissors":
    print("Draw!")

elif player == "scissors" and computer == "scissors":
    print("Draw!")

elif player == "Rock" and computer == "rock":
    print("Draw!")

elif player == "rock" and computer == "rock":
    print("Draw!")

elif player == "Paper" and computer == "paper":
    print("Draw!")

elif player == "paper" and computer == "paper":
    print("Draw!")

elif player == "Rock" and computer == "scissors":
    print("You win!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "Scissors" and computer == "paper":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player == "Paper" and computer == "rock":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "Paper" and computer == "scissors":
    print("You lose!")

elif player == "paper" and computer == "scissors":
    print("You lose!")

elif player == "Scissors" and computer == "rock":
    print("You lose!")

elif player == "scissors" and computer == "rock":
    print("You lose!")

elif player == "Rock" and computer == "paper":
    print("You lose!")

elif player == "Rock" and computer == "paper":
    print("You lose!")

else:
    print("ERROR")
