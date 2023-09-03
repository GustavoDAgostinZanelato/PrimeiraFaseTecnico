codigo = []
nome = []
peso = []

for i in range(3):
    cod = int(input("Código Aluno: "))
    codigo.append(cod) #append serve para inserir um elemento no vetor
    nom = input("Nome Aluno: ")
    nome.append(nom)
    pes = float(input("Peso Aluno: "))
    peso.append(pes)

print("Código \tNome\t\t\tPeso") #\t é um espaço entre as linhas, como um TAB
for i in range(3):
    print(codigo[1],"\t",nome[i], "\t\t\t", peso[i])

