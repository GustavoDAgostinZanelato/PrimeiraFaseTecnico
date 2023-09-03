numeros = []

def main():
    
    for i in range(10):
        while True:
            auxnumeros = int(input("Digite um numero: "))
        
            procurar = auxnumeros
        
            if procurar in numeros:
                print("valor repetido. Digite Novamente")
            else:
                numeros.append(auxnumeros)
                break
                
    print(numeros)
main()
        