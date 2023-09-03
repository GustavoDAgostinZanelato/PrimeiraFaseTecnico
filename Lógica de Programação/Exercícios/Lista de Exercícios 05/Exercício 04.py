def somaImposto (taxa,valor):
    return valor * (1+(taxa/100))

def main ():
    valorvenda = float(input("informe o valor da Venda: "))
    imposto = float(input("Informe o valor de Imposto: "))
    valorfinal = somaImposto(imposto,valorvenda)
    print("Valor final da venda com imposto é de: ", valorfinal)

main ()
