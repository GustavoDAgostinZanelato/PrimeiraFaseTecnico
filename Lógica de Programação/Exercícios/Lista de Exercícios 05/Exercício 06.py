def calcIR(salbruto):
    return salbruto * 0.11
def calcINSS(salbruto):
    return salbruto * 0.08
def calcSindicato(salbruto):
    return salbruto * 0.05

def main ():
    horatrabalhada = int(input("Digite o total de horas trabalhadas: "))
    valorhora = float(input("Digite o valor da hora trabalhada: "))
    salbruto = horatrabalhada * valorhora
    ir = calcIR(salbruto)
    inss = calcINSS(salbruto)
    sindicato = calcSindicato(salbruto)
    salliquido = salbruto - (ir+inss+sindicato)

    print("Salário Bruto R$", salbruto)
    print("IR R$", ir)
    print("INSS R$", inss)
    print("Sindicato R$", sindicato)
    print("Salário Líquido R$", salliquido)

main()

