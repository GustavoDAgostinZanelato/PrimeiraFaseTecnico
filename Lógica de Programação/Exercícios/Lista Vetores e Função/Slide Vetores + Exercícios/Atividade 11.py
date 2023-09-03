numeros = []
qtd_negativos = 0
soma_positivos = 0

for i in range (10):
    while True:
        valor = float(input("Digite um valor real qualquer: "))
        numeros.append(valor)
        
        if(valor < 0):
            qtd_negativos = qtd_negativos + 1
            break
        
        elif(valor > 0):
            soma_positivos = soma_positivos + valor
            break
        
print(numeros)            
print("A quantidade de números negativos na lista é de:", qtd_negativos)
print("A soma dos números positivos da lista é de:", soma_positivos)
        
        
        
