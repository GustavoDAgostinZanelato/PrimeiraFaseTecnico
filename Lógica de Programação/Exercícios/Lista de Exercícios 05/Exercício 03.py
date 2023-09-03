def verificar (valor):
    if (valor<0):
        return "Negativo"
    elif (valor>0):
        return "Positivo"
    else:
        return "Nulo"

def main ():
    valor = int(input("Digite um número: "))
    resposta = verificar(valor)
    print ("O número", valor, "é", resposta)
main ()