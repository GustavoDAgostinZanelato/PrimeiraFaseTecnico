#Gustavo D'Agostin Zanelato - Matrícula: 50390

#def para identificar o dia da semana:
def dias_semana(numero):
    if(numero == 1):
        return "Seu número é equivalente a: Segunda-Feira"
    elif(numero == 2):
        return "Seu número é equivalente a: Terça-Feira"
    elif(numero == 3):
        return "Seu número é equivalente a: Quarta-Feira"
    elif(numero == 4):
        return "Seu número é equivalente a: Quinta-Feira"
    elif(numero == 5):
        return "Seu número é equivalente a: Sexta-Feira"
    elif(numero == 6):
        return "Seu número é equivalente a: Sábado"
    elif(numero == 7):
        return "Seu número é equivalente a: Domingo"
    else:
        return "ERRO. Número Inválido, tente novamente."

#Atribuindo um valor a variável "numero":
numero = int(input("Informe um número de 1 a 7 ao programa: "))

#Atribuindo valores ao def:
dias_semana(numero)

#Resultado do programa:
resposta = dias_semana(numero)
if resposta:
    print(resposta)