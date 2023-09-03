def ler_vetor():
    vetor = []

    for i in range(20):
        valor = int(input(f"Digite o valor {i + 1}: "))
        vetor.append(valor)

    return vetor


def eliminar_elementos_repetidos(vetor):
    vetor_sem_repeticao = []

    for valor in vetor:
        if valor not in vetor_sem_repeticao:
            vetor_sem_repeticao.append(valor)

    return vetor_sem_repeticao


vetor = ler_vetor()

vetor_sem_repeticao = eliminar_elementos_repetidos(vetor)

print("Elementos do vetor sem repetição:")
for valor in vetor_sem_repeticao:
    print(valor)
