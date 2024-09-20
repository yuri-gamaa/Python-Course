# Story of Tresuare Island

from art import treasure_map_art

print(treasure_map_art, '\n\n')

print("""
Story:
      
You arrived to a island in no where to find a treasure. You choose your
on way to the treasure, which one will be?\n\n
""")

if input("There is a path that leads to two oposite directions: which one you choose:\n\n\tleft or right?\n\n: ") == 'left':
    if input("You choose right, now you found a lake, which one you choose:\n\n\tswim or wait?\n\n: ") == 'swim':
        if input('Ok, you choose swim rather than wait and you found a chest walking across the lake. '
                 'Which one choose:\n\n\topen or go away?\n\n: ') == 'open':
            print('Congratulations, you found the treasure.')
        else:
            print('The treasure was there, you choose go away. You just lost your time, it was all for nothing.')
    else:
        print('You lose. You waited to much and died of hunger.')
else:
    print('You lose. You went to a jungle an died hunted by a wild animal.')