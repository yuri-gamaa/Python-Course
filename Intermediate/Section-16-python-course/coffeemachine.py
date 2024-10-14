from prettytable import PrettyTable


class CoffeeMachine:
    
    def __init__(self):
        self.water = 1000       # ml
        self.milk = 500         # ml
        self.coffee = 99        # g
        self.money = 0          # $

    @staticmethod
    def check_payment(profit):
        print("How many coins of...")
        pennies = int(input("Pennies: "))  # 1 cent
        nickels = int(input("Nickels: "))  # 5 cent
        dimes = int(input("Dimes: "))  # 10 cent
        quarters = int(input("Quarters: "))  # 25 cent

        total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

        if total < profit:
            return False
        else:
            return True

    def transaction(self, order, ml_water, ml_milk, gram, profit):

        payment = self.check_payment(profit)

        if payment:
            if self.water - ml_water < 0 or self.milk - ml_milk < 0 or self.coffee - gram < 0:
                print("Not ingredients enough.")
            else:
                print("Let's go.")
                self.water -= ml_water
                self.milk -= ml_milk
                self.coffee -= gram
                self.money += profit
                print(f'Here is your {order}.')
        else:
            print("Not money enough.")

    def report(self):
        ptt = PrettyTable()
        ptt.add_column("Water", [f'{self.water}ml'])
        ptt.add_column("Milk", [f'{self.milk}ml'])
        ptt.add_column("Coffee", [f'{self.coffee}g'])
        ptt.add_column("Total ($)", [f'${self.money:.2f}'])
        print(ptt)
