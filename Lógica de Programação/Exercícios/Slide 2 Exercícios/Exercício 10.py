count_criciuma = 0
count_tubarao = 0
count_florianopolis = 0

for i in range(50):
    nome = input("Por favor, insira o nome da pessoa #" + str(i + 1) + ": ")
    cidade = input("Por favor, insira a cidade de " + nome + ": ")
    estado = input("Por favor, insira o estado de " + nome + ": ")

    if cidade.lower() == "criciúma":
        count_criciuma += 1
    elif cidade.lower() == "tubarão":
        count_tubarao += 1
    elif cidade.lower() == "florianopolis":
        count_florianopolis += 1

print("Resultado:")
print(str(count_criciuma) + " pessoas moram em Criciúma")
print(str(count_tubarao) + " pessoas moram em Tubarão")
print(str(count_florianopolis) + " pessoas moram em Florianópolis")
