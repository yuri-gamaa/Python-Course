def exibir_fichas(total):

    FICHAS_VALORES = [1.0, 2.5, 5.0, 10.0, 25.0, 50.0, 100.0, 250.0, 500.0]
    CYAN = '\033[96m'
    END = '\033[0m'

    fichas = [
        ["1) R$ 1.00"],
        ["2) R$ 2,50"],
        ["3) R$ 5,00"],
        ["4) R$ 10,00"],
        ["5) R$ 25,00"],
        ["6) R$ 50,00"],
        ["7) R$ 100,00"],
        ["8) R$ 250,00"],
        ["9) R$ 500,00"]
    ]

    for i in range(len(FICHAS_VALORES)):
        if total >= FICHAS_VALORES[i]:
            fichas[i][0] = CYAN + str(fichas[i][0]) + END


        catalogo = f"""\n
Fichas:

{fichas[0][0]}
{fichas[1][0]}
{fichas[2][0]}
{fichas[3][0]}
{fichas[4][0]}
{fichas[5][0]}
{fichas[6][0]}
{fichas[7][0]}
{fichas[8][0]}

Digite \'q\' para concluir a aposta.
Digite \'i\' para exibir o catalago novamente.\n
"""  
    print(catalogo)


def alterar_cartas(mao):
    string = ''
    for carta in mao:
        if carta == 11.0 or carta == 1.0:
            string += 'A '
        elif carta == 10.01:
            string += 'J '
        elif carta == 10.011:
            string += 'Q '
        elif carta == 10.001:
            string += 'K '
        else:
            string += str(int(carta)) + ' '

    return string


def exibir_jogo(mesa, jogador, mesa_s, jogador_s, aposta, deposito, primeira=None, mostrar_mesa=None):

    if mostrar_mesa:
        mao_mesa = alterar_cartas(mesa)
        resultado_mesa = str(mesa_s)
        vez = 'MESA'
    else:
        mao_mesa = '?'
        resultado_mesa = '?'
        vez = 'JOGADOR'

    if primeira:
        dobrar = "D - Dobrar aposta"
    else:
        dobrar = ""

    print(f"""
          
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          
Vez: {vez}                              Opções:

                                        P - Pedir carta
                                        M - Manter mão
                                        {dobrar}
Total: {resultado_mesa}
Mesa: {mao_mesa}                


Total: {jogador_s}
Jogador: {alterar_cartas(jogador)}
                                        Aposta:   ${float(aposta):.2f}
                                        Depósito: ${float(deposito):.2f}
    """)


def checar_jogo(soma, rodada, jogada=None, mesa=None):

    if soma == 21:
        return 100
    elif soma > 21:
        return 100
    elif jogada == 'D':
        return 100
    elif mesa and soma >= 17:
            return 100
    else:
        return rodada + 1


def caso_As(mao):

    if sum(mao) > 21.0 and 11.0 in mao:
        for carta in range(len(mao)):
            if mao[carta] == 11.0:
                mao[carta] = 1.0
    return mao
