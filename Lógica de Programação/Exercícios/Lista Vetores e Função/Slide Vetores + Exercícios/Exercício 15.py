def ler_vetor():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite o valor {i + 1}: "))
        vetor.append(valor)

    return vetor


def calcular_vetor_c(vetor_a, vetor_b):
    vetor_c = []

    for i in range(10):
        c = vetor_a[i] - vetor_b[i]
        vetor_c.append(c)

    return vetor_c

print("Digite os valores do vetor A:")
vetor_a = ler_vetor()


print("Digite os valores do vetor B:")
vetor_b = ler_vetor()


vetor_c = calcular_vetor_c(vetor_a, vetor_b)


print("Dados do vetor C:")
for valor in vetor_c:
    print(valor)
