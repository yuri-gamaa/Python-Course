# def alterar_fichas(total):

#     CYAN = '\033[96m'
#     GRAY = '\033[97m'
#     END = '\033[0m'

#     fichas = [
#         ["A) R$ 1.00"],
#         ["B) R$ 2,50"],
#         ["C) R$ 5,00"],
#         ["D) R$ 10,00"],
#         ["E) R$ 25,00"],
#         ["F) R$ 50,00"],
#         ["G) R$ 100,00"],
#         ["H) R$ 250,00"],
#         ["I) R$ 500,00"]
#     ]

#     #                   0   1   2      3    4      5     6      7       8
#     fichas_valores = [1.0, 2.5, 5.0, 10.0, 25.0, 50.0, 100.0, 250.0, 500.0]

#     for i in range(len(fichas_valores)):
#         if total <= fichas_valores[i]:
#             fichas[i][0] = GRAY + fichas[i][0] + END
#         else:
#             fichas[i][0] = CYAN + fichas[i][0] + END
    
#     catalogo = f"""
# Fichas:

# {fichas[0][0]}
# {fichas[1][0]}
# {fichas[2][0]}
# {fichas[3][0]}
# {fichas[4][0]}
# {fichas[5][0]}
# {fichas[6][0]}
# {fichas[7][0]}
# {fichas[8][0]}

# Digite \'q\' para concluir a aposta.\n
# """

#     print(catalogo)

# # alterar_fichas(500.0)

# comida = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# stop = int(input(": "))

# for x in comida[:stop+1]:
#     print(x)

# mesa = [baralho[carta] for carta in range(1, 4, 2)]
# jogador = [baralho[carta] for carta in range(0, 3, 2)]

baralho = [11.0, 11.0, 10, 33]
def caso_As(mao):

    if sum(mao) > 21.0 and 11.0 in mao:
        for carta in range(len(mao)):
            if mao[carta] == 11.0:
                mao[carta] = 1.0

    return mao

# print(caso_As(baralho))

