# Password Generator

import sys
import random as ran

lletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.', '_', "=", "-"]

m_n = sys.argv[1]

qt = []

qt.append(int(m_n[0]))
qt.append(int(m_n[1]))
qt.append(int(m_n[2]))
qt.append(int(m_n[3]))

passwd = []

for l in range(0, qt[0]):
    passwd.append(ran.choice(Uletters))

for l in range(0, qt[1]):
    passwd.append(ran.choice(lletters))

for n in range(0, qt[2]):
    passwd.append(ran.choice(numbers))

for s in range(0, qt[3]):
    passwd.append(ran.choice(symbols))

ran.shuffle(passwd)
rst = ''

for roll in range(0, len(passwd)):
    rst += passwd[roll]

print("\n" + rst)