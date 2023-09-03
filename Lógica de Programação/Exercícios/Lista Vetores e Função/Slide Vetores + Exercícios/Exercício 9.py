valores = []

for i in range(6):
    while True:
        
        valor = int(input("Digite um valor inteiro par: "))
        if((valor % 2) == 0):
            valores.append(valor)
            break
        else:
            print("Número Ímpar ou Inválido. Tente novamente")

print("Valores na ordem reversa:")
for valor in reversed(valores):
    print(valor)