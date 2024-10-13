# Password Generator

import random as ran

lletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.', '_', "=", "-"]


def new_pass():
    qt = 3

    upper = [ran.choice(Uletters) for c in range(0, qt)]
    lower = [ran.choice(lletters) for c in range(0, qt)]
    nums = [ran.choice(numbers) for c in range(0, qt)]
    sym = [ran.choice(symbols) for c in range(0, qt)]

    passwd = upper + lower + nums + sym

    ran.shuffle(passwd)
    rst = ''.join(passwd)

    return rst
