maiores_idade = 0
menores_idade = 0

for i in range(10):
    nome = input("Por favor, insira o nome da pessoa #" + str(i + 1) + ": ")
    idade = int(input("Por favor, insira a idade de " + nome + ": "))

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print("Resultado:")
print(str(maiores_idade) + " pessoas são maiores de idade")
print(str(menores_idade) + " pessoas são menores de idade")
