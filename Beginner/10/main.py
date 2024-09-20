from art import logo

print(logo, "\n")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mult(a, b):
    conta = a * b
    print(conta)    # FUNCIONA
    return a * b + 100

def div(a, b):
    return a / b

operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

# for op in operation:
#     print(op)

def calculation():
    fst_num = int(input("1º: "))

    keep_going = False

    while not keep_going:

        op_symbol = input("Operation: ")
        other_num = int(input("Number: "))

        calc = operation[op_symbol]
        rs = calc(fst_num, other_num)

        print(f'{fst_num} {op_symbol} {other_num} = {rs}')

        decision = input("Continue the previous calculation? (y|n) ").lower()

        if decision == "y":
            fst_num = rs
            keep_going = False
        else:
            keep_going = True

    if input("Close calculator? (y|n) ").lower() == "y":
        print("Finished.")
    else:
        calculation()

calculation()