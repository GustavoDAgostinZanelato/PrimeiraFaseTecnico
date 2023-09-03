def ler_vetor():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite o valor {i + 1}: "))
        vetor.append(valor)

    return vetor

def unir_vetores(vetor_a, vetor_b):
    uniao = list(set(vetor_a + vetor_b))

    return uniao


print("Digite os valores do primeiro vetor:")
vetor_a = ler_vetor()

print("Digite os valores do segundo vetor:")
vetor_b = ler_vetor()

uniao = unir_vetores(vetor_a, vetor_b)

print("União entre os dois vetores:")
for valor in uniao:
    print(valor)
