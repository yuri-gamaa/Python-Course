import random as rd
from art import logo, vs

print(logo, "\n")

print("Jogo de perguntas e respostas, acerte a opção verdadeira e acumule pontos até errar.\n")

banco_de_questoes =  {                                                                                      # RESPOSTAS CORRETAS:
    "Qual é melhor": ["Toddy", "Nescal"],                                                                   # 0
    "Quem venceu a última disputa no boxe?": ["Anderson Silva", "Chael Sonnen"],                            # 0
    "Quanto é: 2 x 2 + 1 x 10": ["60", "14"],                                                              # 1
    "Qual deles nomeia a fobia de uma pessoa que tem pavor da noite": ["Nictofobia", "Mictofobia"],         # 0
    "Em GOT, qual dos personagens representou Tyrion Lannister do jugamento de regicídio": ["Bronn", "Príncipe Oberyn"]    # 1
}

gabarito = {
    "Qual é melhor": 0,
    "Quem venceu a última disputa no boxe?": 0,
    "Quanto é: 2 x 2 + 1 x 10": 1,
    "Qual deles nomeia a fobia de uma pessoa que tem pavor da noite": 0,
    "Em GOT, qual dos personagens representou Tyrion Lannister do jugamento de regicídio": 1
}

def comparar_respostas(pergunta, resposta):
    if resposta == "A":
        resposta = 0
    elif resposta == "B":
        resposta = 1

    for p in gabarito:
        if p == pergunta:
            if resposta == gabarito[p]:
                return True
            else:
                return False

pontuacao = 0

for pergunta in banco_de_questoes:

    print(f"""\n\n
A) {banco_de_questoes[pergunta][0]}

{vs}

B) {banco_de_questoes[pergunta][1]}


""")
    resposta = input(f'{pergunta}? \"A\" ou \"B\": ').upper()
    resposta_avaliada = comparar_respostas(pergunta, resposta)

    if not resposta_avaliada:
        print(f'\nErrou! Vc conseguiu {pontuacao} acertos.')
        break
    elif not resposta_avaliada and pontuacao == 0:
        print("\nHaha vc não acertou nada.")
    else:
        pontuacao+=1
        print(f'\nBoa, Vc conseguiu {pontuacao} acertos.')