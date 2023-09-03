def expressao(n):
    soma=0
    for i in range(n):
        if (i > 1):
            soma += i/(i+i-1)
    return soma

def main():
    n = int(input("Informe o número de vezes"))
    operacao = expressao(n)
    print("O valor é", operacao)

main()