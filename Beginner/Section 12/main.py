import art
from random import randint

print(art.logo, "\n")

verify = False

while not verify:
    difficult = str(input("Game mode:\n\n- Easy (type \'E\')\n- Hard (type \'H\')\n\n: ")).upper()
    
    if difficult == "E":
        turn = 10
        verify = True
    elif difficult == "H":
        turn = 5
        verify = True
    else:
        print("\nOnly \"E\" or \"H\" options available, dumbass.\n")

final_turn = 0
right_number = randint(1, 100)

print("\nChoose a number between 1 to 100, if you guess what number is you win, if not you lose. Good luck!\n\n")

while turn > final_turn:
    choosen_number = int(input(": "))

    if choosen_number == right_number:
        print("\nCongratulations, you won!")
        break
    elif choosen_number != right_number and (turn-1) == final_turn:
        print("Congratulations, you lose!")
    elif choosen_number > right_number:
        print(f'Too high. You can guess more {turn-1} times.')
    elif choosen_number < right_number:
        print(f'Too low. You can guess more {turn-1} times.')

    turn-=1