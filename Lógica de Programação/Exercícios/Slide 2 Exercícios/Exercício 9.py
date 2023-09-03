count_masculino = 0
count_feminino = 0

for i in range(10):
    nome = input("Por favor, insira o nome da pessoa #" + str(i + 1) + ": ")
    sexo = input("Por favor, insira o sexo de " + nome + " (M para masculino ou F para feminino): ")

    if sexo.upper() == "M":
        count_masculino += 1
    elif sexo.upper() == "F":
        count_feminino += 1
    else:
        print("Sexo inválido para " + nome)

print("Resultado:")
print(str(count_masculino) + " pessoas são do sexo masculino")
print(str(count_feminino) + " pessoas são do sexo feminino")
