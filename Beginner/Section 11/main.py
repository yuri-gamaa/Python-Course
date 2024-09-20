import detalhes as dh
from random import shuffle

def apostar_partida(total):

    dh.exibir_fichas(total)

    apostas = []

    verdadeiro = True
    while verdadeiro:
        
        apostar = input(": ")

        match apostar:

            case '1':
                apostas.append(1.0)
            case '2':
                apostas.append(2.5)
            case '3':
                apostas.append(5.0)
            case '4':
                apostas.append(10.0)
            case '5':
                apostas.append(25.0)
            case '6':
                apostas.append(50.0)
            case '7':
                apostas.append(100.0)
            case '8':
                apostas.append(250.0)
            case '9':
                apostas.append(500.0)
            case 'q':
                if sum(apostas) == 0:
                    print("\nÉ preciso adicionar algum valor.\n")
                else:
                    verdadeiro = False
            case 'i':
                dh.exibir_fichas(total)
            case _:
                print("\nOpção inválida.\n")

        aposta_total = sum(apostas)
        if aposta_total > total:
            aposta_total -= apostas[-1]
            apostas[-1] = 0
            print("\nVocê não possui a quantia mínima.\n")
        elif aposta_total == total:
            verdadeiro = False

        print(f'Aposta: {aposta_total:.2f}\n')

    return aposta_total


def definir_vencedor(mesa, jogador, resultado, aposta):

    if mesa == jogador:
        print('\nEmpate.')
        resultado += aposta

    elif mesa > jogador and mesa <= 21 or jogador > 21 and mesa <= 21:
        print("\nMesa Vence.")
    
    elif mesa < jogador and jogador <= 21 or mesa > 21 and jogador <= 21:
        print("\nJogador Vence.")
        resultado += (aposta*2)
    
    return resultado


def blackjack(deposito):

    baralho = [11.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.01, 10.011, 10.001,
               11.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.01, 10.011, 10.001,
               11.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.01, 10.011, 10.001,
               11.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.01, 10.011, 10.001]

    shuffle(baralho)

    aposta = apostar_partida(deposito)
    deposito -= aposta
    mesa = [baralho[carta] for carta in range(1, 4, 2)]
    jogador = [baralho[carta] for carta in range(0, 3, 2)]

    mesa = dh.caso_As(mesa)
    jogador = dh.caso_As(jogador)
    
    soma_mesa = int(sum(mesa))
    soma_jogador = int(sum(jogador))

    dh.exibir_jogo(mesa, jogador, soma_mesa, soma_jogador, aposta, deposito, primeira=True)

    # COMEÇAR A MONTAR AS JOGADAS
    # JOGADOR
    rodada = 0
    while rodada < 100:
        jogada = input("\n: ").upper()
        posicao = rodada + 4
            
        match jogada:

            case 'P':
                jogador.append(baralho[rodada + 4])
                soma_jogador += int(jogador[-1])
            case 'M':
                rodada = 100

        if rodada == 0 and jogada == 'D':
            if (deposito - aposta) < 0:
                print('\nVocê não possui fichas suficientes.')
                continue
            else:
                jogador.append(baralho[rodada + 4])
                deposito -= aposta
                aposta += aposta
                rodada = 100

        elif rodada > 0 and jogada == 'D':
            print("\nEssa opção não está disponível.")

        jogador = dh.caso_As(jogador)
        soma_jogador = int(sum(jogador))
        dh.exibir_jogo(mesa, jogador, soma_mesa, soma_jogador, aposta, deposito)

        rodada = dh.checar_jogo(soma_jogador, rodada, jogada)

    # MESA
    rodada = 0
    while rodada < 100:

        rodada = dh.checar_jogo(soma_mesa, rodada, mesa=True)

        mesa = dh.caso_As(mesa)
        soma_mesa = int(sum(mesa))
        dh.exibir_jogo(mesa, jogador, soma_mesa, soma_jogador, aposta, deposito, mostrar_mesa=True)

        if rodada != 100:
            posicao += 1
            mesa.append(posicao)
        else:
            break

        input("\n\'Enter\'")
    
    resultado = definir_vencedor(soma_mesa, soma_jogador, deposito, aposta)
    
    print(f"Quantia: ${resultado:.2f}\nAposta: ${aposta:.2f}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    input("\nPressione \'Enter\' para voltar recomeçar a partida.")

    return resultado


quantia = float(input("Defina a quantia do seu depósito: "))

jogar = True
while jogar:
    if quantia < 1.0:
        print("\nInfelizmente vc não possui o bastante para jogar.")
        jogar = False
    else:
        quantia = blackjack(quantia)
