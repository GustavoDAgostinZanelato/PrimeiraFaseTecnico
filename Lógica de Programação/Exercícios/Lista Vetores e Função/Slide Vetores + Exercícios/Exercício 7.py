num_int = []
maior_num = 0

for i in range(10):
    numero = int(input("Escreva um número inteiro: "))
    num_int.append(numero)
    
    if(maior_num < numero):
        maior_num = numero
    else:
        maior_num = maior_num

print(num_int)

for i in range(len(num_int)):
    if(maior_num == num_int[i]):
        print("O maior valor é",maior_num, "e está localizado na casa", i, "da lista")
    

