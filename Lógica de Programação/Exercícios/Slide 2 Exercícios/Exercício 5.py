nomes = []
medias = []

for i in range(10):
    nome = input("Por favor, insira o nome do aluno #" + str(i + 1) + ": ")
    media = float(input("Por favor, insira a média final de " + nome + ": "))

    nomes.append(nome)
    medias.append(media)

print("Situação dos Alunos:")
for i in range(10):
    if medias[i] < 7:
        print(nomes[i] + " foi REPROVADO(a) com média final " + str(medias[i]))
    else:
        print(nomes[i] + " foi APROVADO(a) com média final " + str(medias[i]))
