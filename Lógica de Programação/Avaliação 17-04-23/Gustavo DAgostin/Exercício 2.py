#área de seleção das variáveis:
A = V = O = 0
L = C = P = 0
situacao3 = 0

npessoas = int(input("Quantas pessoas foram entrevistadas? "))

#Coletando dados:
for i in range (npessoas):
    sexo = str(input("Qual o seu sexo, Masculino (M) OU Feminino (F): "))
    olhos = str(input("A- Azuis \nV- Verdes \nO- Outros \nQual a cor dos seus olhos: "))
    cabelo = str(input("L- Louros \nC- Castanhos \nP- Pretos \nQual a cor do seu cabelo: "))

#Cor dos olhos:
    if (olhos == "A"):
        A = A + 1

    elif (olhos == "V"):
        V = V + 1

    elif (olhos == "O"):
        O = O + 1

#Cor do cabelo:
    if (cabelo == "L"):
        L = L + 1

    elif (cabelo == "C"):
        C = C + 1

    elif (cabelo == "P"):
        P = P =1

#Sexo feminino com cabelo loiro e alhos azuis:
    if (sexo == "F"):
        if (olhos == "A"):
            if (cabelo == "L"):
                situacao3 = situacao3 + 1

#Texto com as respostas:
print("Número de pessoas que tem olhos Azuis: ", A)
print("Número de pessoas que tem olhos Verdes: ", V)
print("Número de pessoas que tem outra cor de olhos: ", O)

print("Número de pessoas com cor de cabelo igual a louros: ", L)
print("Número de pessoas com cor de cabelo igual a castanhos: ", C)
print("Número de pessoas com cor de cabelo igual a preto: ", P)

print("Número de mulheres loiras com olhos azuis: ", situacao3)


