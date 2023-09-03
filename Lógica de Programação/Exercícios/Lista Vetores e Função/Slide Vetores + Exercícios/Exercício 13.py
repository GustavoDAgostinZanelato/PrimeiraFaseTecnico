def verificar_valores_iguais(vetor):
    valores_iguais = []

    for i in range(len(vetor)):
        if vetor.count(vetor[i]) > 1 and vetor[i] not in valores_iguais:
            valores_iguais.append(vetor[i])

    return valores_iguais

def ler_vetor():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite o valor {i + 1}: "))
        vetor.append(valor)

    return vetor

vetor = ler_vetor()

valores_iguais = verificar_valores_iguais(vetor)

if len(valores_iguais) > 0:
    print("Valores iguais encontrados:")
    for valor in valores_iguais:
        print(valor)
else:
    print("Não foram encontrados valores iguais.")
