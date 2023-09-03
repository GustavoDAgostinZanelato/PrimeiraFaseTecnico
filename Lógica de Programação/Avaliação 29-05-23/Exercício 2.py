#Gustavo D'Agostin Zanelato - Matrícula: 50390

#Seleção de variáveis
qtdpessoas = int(input("Quantas pessoas foram intrevistadas: "))
contador = 0
somaidadesM = 0
somaidadesF = 0
numeroM = 0
numeroF = 0

#Função While
while (contador < qtdpessoas):
    nome = str(input("Insira o nome: "))
    sexo = str(input("Insira o sexo \nM-Masculino \nF-Feminino "))
    idade = int(input("Qual a idade: "))
    contador = contador + 1

    if (sexo == "M"):
        somaidadesM = somaidadesM + idade
        numeroM = numeroM + 1
    else:
        somaidadesF = somaidadesF + idade
        numeroF = numeroF + 1


mediaidadeM = somaidadesM / numeroM
mediaidadeF = somaidadesF / numeroF

#Resultados Obtidos:
print("A média de idade Masculina é: ", mediaidadeM)
print("A média de idade Feminina é: ", mediaidadeF)