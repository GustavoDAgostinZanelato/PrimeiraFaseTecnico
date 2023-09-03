#Gustavo D'Agostin Zanelato - Matrícula: 50390

#def para verificar se a variável "letra" é uma vogal ou consoante:
def verificacao (letra):
    if(letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
        return "Sua letra é uma Vogal."

    elif(letra == "B") or (letra == "C") or (letra == "D") or (letra == "F") or (letra == "G") or (letra == "H") or (letra == "I") or (letra == "J") or (letra == "K") or (letra == "L") or (letra == "M") or (letra == "N") or (letra == "P") or (letra == "Q") or (letra == "R") or (letra == "S") or (letra == "T") or (letra == "V") or (letra == "W") or (letra == "X") or (letra == "Y") or (letra == "Z"):
        return "Sua letra é uma Consoante."

    else:
        return "ERRO. Infome uma caracter válido." #Mensagem de ERRO caso o caracter seja inpróprio ao programa.

#Coletando o valor da variável "letra":
letra = str(input("Insira uma letra do alfabeto: "))

#Atribuindo valores ao def:
verificacao(letra)

#Resultado do programa:
resposta = verificacao(letra)
if resposta:
    print(resposta)
