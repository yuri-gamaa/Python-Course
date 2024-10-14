# Espresso     ->      $1.50
# Latte        ->      $2.50
# Cappuccino   ->      $3.00


from coffeemachine import *

cm = CoffeeMachine()
verify = True

while verify:
    order = input("What type you want? ").lower()

    if order == "espresso":
        # Do espresso
        cm.transaction(order, ml_water=50, ml_milk=0, gram=18, profit=1.5)
    elif order == "latte":
        # Do latte
        cm.transaction(order, ml_water=200, ml_milk=150, gram=24, profit=2.5)
    elif order == "cappuccino":
        # Do cappuccino
        cm.transaction(order, ml_water=250, ml_milk=100, gram=24, profit=3.0)
    elif order == "report":
        # Show resources
        cm.report()
    elif order == "off":
        # End machine
        verify = False
    else:
        print("This option is not allowed.\n")
