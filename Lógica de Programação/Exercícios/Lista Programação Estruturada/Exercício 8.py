def verificacao(valor):
    if(valor>0):
        return True     # True e False são as variáveis booleanas
    else:
        return False
        
valor = int(input("Digite um valor inteiro: "))
verificacao(valor)

resultado = verificacao(valor)

if resultado:
    print("O valor é Positivo")
else:
    print("O valor é Negativo")