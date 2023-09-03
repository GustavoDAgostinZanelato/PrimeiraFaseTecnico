nomes = []
vetoraux = []

def main():
    for i in range(10):
        nomes.append(input("Digite um nome: "))
    numcar = int(input("Digite o número de caracteres: "))
    for i in range (10):
        if(numcar <= len(nomes[i])):
            vetoraux.append(nomes[i])
    print(nomes)
    print(vetoraux)

main()
