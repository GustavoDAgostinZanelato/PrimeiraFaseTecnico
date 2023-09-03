ipi = float(input("Digite a porcentagem do IPI a ser acrescido no valor das peças: "))
cod1 = int(input("Digite o código da peça 1: "))
valor1 = float(input("Digite o valor unitário da peça 1: "))
quant1 = int(input("Digite a quantidade de peças 1: "))
cod2 = int(input("Digite o código da peça 2: "))
valor2 = float(input("Digite o valor unitário da peça 2: "))
quant2 = int(input("Digite a quantidade de peças 2: "))

valor_total = (valor1 * quant1 + valor2 * quant2) * (ipi/100 + 1)

print("O valor total da compra é R$", valor_total)


