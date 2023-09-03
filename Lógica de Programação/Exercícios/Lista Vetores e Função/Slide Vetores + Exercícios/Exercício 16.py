def ler_vetor():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite o valor {i + 1}: "))
        vetor.append(valor)

    return vetor


def encontrar_intersecao(vetor_a, vetor_b):
    intersecao = []

    for valor in vetor_a:
        if valor in vetor_b and valor not in intersecao:
            intersecao.append(valor)

    return intersecao


print("Digite os valores do primeiro vetor:")
vetor_a = ler_vetor()


print("Digite os valores do segundo vetor:")
vetor_b = ler_vetor()


intersecao = encontrar_intersecao(vetor_a, vetor_b)


print("Interseção entre os dois vetores:")
for valor in intersecao:
    print(valor)
