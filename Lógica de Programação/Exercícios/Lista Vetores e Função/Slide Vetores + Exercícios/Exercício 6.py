num_int = []
maior_numero = 0
menor_numero = 0

for i in range(10):
    numero = int(input("Escreva um número inteiro: "))
    num_int.append(numero)
    
    if(maior_numero < numero):
        maior_numero = numero
    else:
        maior_numero = maior_numero
        
    if(menor_numero > numero):
        menor_numero = numero
    else:
        menor_numero = menor_numero
        
print("O menor número da sequência é: ", menor_numero)
print("O maior número de saquência é: ", maior_numero)

   
    