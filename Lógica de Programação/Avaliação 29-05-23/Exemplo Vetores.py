numeros = [3,10,1,2,5,7,2,-10,30,99]

print(numeros) #irá mostrar toda a sequecia
print(numeros[1]) #vai mostrar o número na casa 1. A contagem  da sequência começa do zero
print(numeros[4], numeros[0], numeros [9]) #mostra os numeros nas casas correspondetes
print(len(numeros)) #mostra quantos números tem na sequência


num = int(input("Número a procurar: ")) #procura o numero desejado na sequência
achou = 0 #variável caso o número desejado não esteja na sequencia

for i in range(len(numeros)):
    if(num == numeros[i]): #se o numero desejado for lacalizado na sequência, temos o print
        print("Número encontrado no índice:", i)
        achou += 1

if (achou == 0):
    print("Número não encontrado")
else:
    print("Numero econtrado", achou, "vez(es")

