print("Welcome to calculator bill")

bill = float(input("Bill: "))
tip = float(input("Tip, 10, 12 or 15 (%): "))
people = float(input("How many people ate it? "))

bill = bill + ((tip/100) * bill)
bill = bill/people

print(f'Total that each must pay: R${bill:.2f}')