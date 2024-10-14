def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mult(a, b):
    return a * b 

def div(a, b):
    return a / b

fst_num = int(input("1º: "))
snd_num = int(input("2º: "))

op_symbol = input("Operation: ")

# What I've made at first
match op_symbol:

    case '+':
        rs = add(fst_num, snd_num)
    case '-':
        rs = sub(fst_num, snd_num)
    case '*':
        rs = mult(fst_num, snd_num)
    case '/':
        rs = div(fst_num, snd_num)

print(f'{fst_num} {op_symbol} {snd_num} = {rs}')