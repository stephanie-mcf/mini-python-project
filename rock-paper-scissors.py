import random

options = ["rock", "paper", "scissors"]

UserWins = 0
ComputerWins = 0

while True:
    user_choice= input("rock, paper, scissors or q to quit? ")
    if user_choice == "q":
        break
    if user_choice not in options:
        print("Please select a valid option")
        continue
    computer = random.choice(options)
    print("Computer picked: ", computer)

    if user_choice == computer:
        print("It's a tie!")
    elif user_choice == "rock" and computer == "scissors":
        print("You won!")
        UserWins += 1
    elif user_choice == "scissors" and computer == "paper":
        print("You won!")
        UserWins += 1
    elif user_choice == "paper" and computer == "rock":
        print("You won!")
        UserWins += 1
    else:
        print("You lose!")
        ComputerWins +=1

print("Your wins: ", UserWins)
print("Computer wins: ", ComputerWins)
