def verificacao(valor):
    if ((valor % 2)==0):
        return True
    else:
        return False
        
valor = float(input("Digite um valor inteiro: "))
verificacao(valor)

resultado = verificacao(valor)
    
if resultado:
    print("O valor é Par")
else:
    print('O valor é Ímpar')

