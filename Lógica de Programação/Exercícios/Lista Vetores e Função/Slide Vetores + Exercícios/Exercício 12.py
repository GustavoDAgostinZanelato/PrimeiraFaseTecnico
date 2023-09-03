valores = []
maior_valor = 0
menor_valor = 999999999999999999999999999999999999999999999999999999999999999999
soma_valor = 0

for i in range(5):

    valor = float(input(f"Informe o {i+1}º valor da compra: "))
    valores.append(valor)
    
    soma_valor = soma_valor + valor
    
    if(maior_valor < valor):
        maior_valor = valor
    else:
        maior_valor = maior_valor
        
    if(menor_valor > valor):
        menor_valor = valor
    else:
        menor_valor = menor_valor
    
    media = soma_valor/5
print(valores)
print("O maior valor da lista é:", maior_valor)
print("O menor valor da lista é:", menor_valor)
print("A média dos valores é de:", media)