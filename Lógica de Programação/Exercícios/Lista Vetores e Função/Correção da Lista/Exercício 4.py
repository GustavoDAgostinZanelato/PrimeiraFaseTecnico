frase = []

def main():
    frase = input("Digite uma frase: ")
    letra = input("digite uma letra: ")
    total = 0
    for i in range(len(frase)):
        if(frase[i==letra]):
            total += 1
    print("Frase:",frase)
    print("Letra a procurar:",letra)
    print("Total de caracter na frase",total)

main()