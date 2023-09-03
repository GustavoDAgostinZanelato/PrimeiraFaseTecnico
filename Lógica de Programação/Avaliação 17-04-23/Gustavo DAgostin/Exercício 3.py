#área de seleção das variáveis:
anos = anos2 = 0
feminino = masculino = 0
maiorpeso = menorpeso = 0

nalunos = int(input("Qual o número de alunos: "))

#Coletando dados:
for i in range (nalunos):
    nome = str(input("Qual o seu nome: "))
    peso = float(input("Qual o seu peso: "))
    idade = int(input("Quanto anos você tem: "))
    sexo = str(input("M- Masculino \nF- Feminino \nQual o seu sexo: "))

#Alunos com maior ou menor peso:
    if(i == 0):
        maiorpeso = peso
        menorpeso = peso

    else:
        if (peso > maiorpeso):
            maiorpeso = peso

        if (peso < menorpeso):
            menorpeso = peso

#Alunos do sexo masculino ou feminino:
    if (sexo == "M"):
        masculino = masculino + 1

    elif (sexo == "F"):
        feminino = feminino + 1

#Alunos maiores ou menores de idade:
    if (idade >= 18):
        anos = anos + 1

    elif (idade < 18):
        anos2 = anos2 + 1

#Texto com as respostas:
print("Aluno com maior peso: ", maiorpeso)
print("Aluno com menoR peso: ", menorpeso)
print("Número de alunos do sexo mesculino: ", masculino)
print("Número de alunos do sexo feminino: ", feminino)
print("Número de alunos maiores de idade: ", anos)
print("Número de alunos menores de idade: ", anos2)