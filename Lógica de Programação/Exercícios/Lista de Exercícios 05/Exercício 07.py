def calcular(qtde,preco,cond):
    valor = qtde * preco
    if (cond==1):
        valor = valor *0.9
    elif (cond==2):
        valor = valor * 0.95
    else:
        valor = valor * 0.97
    return valor

def main():
    nome = input("Digite o seu nome: ")
    qtde = float(input("Informe a quantidade que você deseja comprar: "))
    preco = float(input("Informe o preço do produto: "))
    while True:
        cond = int(input("Condição de pagamento"
                         "\n1- A vista"
                         "\n2- Cheque"
                         "\n3- Parcelado"
                         "\nCom qual opção você deseja proseguir: "))
        if (cond<1) or (cond>3):
            print("Condição Inválida!")
        else:
            break
    valorfinal = calcular(qtde,preco,cond)
    print("O valor final da compra foi R$", valorfinal)
main()


