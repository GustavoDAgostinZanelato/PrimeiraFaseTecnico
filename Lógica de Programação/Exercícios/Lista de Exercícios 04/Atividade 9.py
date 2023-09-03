soma = 0
quantidade = 0
maior = 0

while True:
    valor = float(input("Digite um valor positivo (ou negativo para sair): "))
    if valor < 0:
        break
    soma += valor
    quantidade += 1
    if valor > maior:
        maior = valor

if quantidade > 0:
    media = soma / quantidade
    print("Média dos valores fornecidos:", media)
    print("Maior valor fornecido:", maior)
else:
    print("Nenhum valor positivo foi fornecido.")
