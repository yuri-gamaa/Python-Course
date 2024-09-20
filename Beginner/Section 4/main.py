# Rock, Paper and Scissors

from random import randint

program_arsenal = ["paper", "scissors", "rock"]
start = 0
result = True
count = 0

while start < 3:

    player = input("Rock, paper or scissors? ").lower()
    program = program_arsenal[randint(0,2)]

    print(f"program: {program}.")

    if program == player:
        start -= 1

    elif player == "rock" and program == "paper":
        print("player lose.\n")
        result = False
    elif player == "rock" and program == "scissors":
        print("player wins.\n")
        result = True

    elif player == "paper" and program == "rock":
        print("player wins\n")
        result = True
    elif player == "paper" and program == "scissors":
        print("player lose.\n")
        result = False

    elif player == "scissors" and program == "rock":
        print("player lose.\n")
        result = False
    elif player == "scissors" and program == "paper":
        print("player wins.\n")
        result = True

    if result:
        count += 1
    elif not result:
        pass

    start += 1

if count > 1:
    print("Player is the champion")
else:
    print("The machine was more cunning than player.")
        