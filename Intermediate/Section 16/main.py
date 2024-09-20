register = {
    "water": 100,    # l
    "milk": 50,      # l
    "coffe": 76,     # 1kg
    "money": 2.5     # $
}


def check_payment(profit):
    print("How many coins of...")
    pennies = int(input("Pennies: "))       #   1 cent
    nickels = int(input("Nickels: "))       #   5 cent
    dimes = int(input("Dimes: "))           #   10 cent
    quarters = int(input("Quarters: "))      #   25 cent

    total = (pennies*0.01) + (nickels*0.05) + (dimes*0.10) + (quarters*0.25)

    if total < profit:
        return False
    else:
        return True


def transaction(order, ml_water, ml_milk, gram, profit):

    payment = check_payment(profit)

    if payment:
        if register["water"] - ml_water < 0 or register["milk"] - ml_milk < 0 or register["coffe"] - gram < 0:
            print("Not ingredients enough.")
        else:
            print("Let's go.")
            register["water"] -= ml_water
            register["milk"] -= ml_milk
            register["coffe"] -= gram
            register["money"] += profit
            print(f'Here is your {order}.')
    else:
        print("Not money enough.")


verify = True
chains = '=-'*30

while verify:
    order = input("What type you want? ").lower()

    if order == "espresso":
        # Do espresso
        transaction(order, ml_water=50, ml_milk=0, gram=18, profit=1.5)
    elif order == "latte":
        # Do latte
        transaction(order, ml_water=200, ml_milk=150, gram=24, profit=2.5)
    elif order == "cappuccino":
        # Do cappuccino
        transaction(order, ml_water=250, ml_milk=100, gram=24, profit=3)
    elif order == "report":
        print(f'{chains}\nReport:')
        for items in register:
            print(f'{items}: {register[items]}')
        print(f'{chains}')
    elif order == "off":
        # End machine
        verify = False
    else:
        print("This option doesn't exist.\n")