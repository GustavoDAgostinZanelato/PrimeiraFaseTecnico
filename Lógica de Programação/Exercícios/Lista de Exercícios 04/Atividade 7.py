import random

saldo = 100
continuar_jogando = True

while continuar_jogando:
    print(f"Saldo atual: R${saldo:.2f}")
    aposta = float(input("Digite o valor da sua aposta: R$"))

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    print(f"Você lançou os dados e obteve {dado1} e {dado2} (total: {soma})")

    if soma == 7 or soma == 11:
        print("Você ganhou!")
        saldo += aposta
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu!")
        saldo -= aposta
    else:
        ponto = soma
        print(f"Seu ponto é {ponto}")
        while True:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            soma = dado1 + dado2
            print(f"Você lançou os dados e obteve {dado1} e {dado2} (total: {soma})")
            if soma == ponto:
                print("Você ganhou!")
                saldo += aposta
                break
            elif soma == 7:
                print("Você perdeu!")
                saldo -= aposta
                break

    if saldo <= 0:
        print("Você ficou sem dinheiro! Fim de jogo.")
        break

    resposta = input("Deseja continuar jogando? (s/n) ")
    if resposta.lower() == 'n':
        print("Fim de jogo.")
        break