import random as rm
from lista import lista
from arte import title, estagios

print(title)

mostrar = []
palavra = rm.choice(lista)
length = range(len(palavra))
cont1 = 0

# Para testes
# print(f'Palavra escholhida: {palavra}')

for x in length:
    mostrar += "_"

while cont1 != 6:

    cont2 = 0
    palpite = input("Escolha uma letra: ").lower()

    for i in length:

        letra = palavra[i]

        if letra == palpite:
            mostrar[i] = letra
            cont2+=1
            
    if cont2 == 0:
        cont1+=1

    if cont1 == 6:
        print("Vc perdeu\n")
    elif '_' not in mostrar:
        print(f"\n\n{' '.join(mostrar)}")
        print(f'\n\nVc ganhou!\n\n{estagios[cont1]}\n')
        break
    
    print(f"\n\n{' '.join(mostrar)}")
    print(f'\n\n{estagios[cont1]}\n\n')