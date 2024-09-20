from art import logo

print(logo)

auction_participant_info = []

def adding_info(participant, amount):
    temp = {}
    temp["name"] = participant
    temp["bid"] = amount
    auction_participant_info.append(temp)

loop = True

while loop:
    name = str(input("Name: "))
    bid = int(input("Bid: "))

    adding_info(name, bid)

    decision = input("Continue adding new participants? (y|n): ").lower()

    if decision == "y":
        loop = True
    else:
        loop = False

vl = []

for bds in range(0, len(auction_participant_info)):
    vl.append(auction_participant_info[bds]["bid"])
    higher = max(vl)
    if vl[bds] == higher:
        id = vl.index(vl[bds])

print(f'\nThe winner is: {auction_participant_info[id]["name"]}.')