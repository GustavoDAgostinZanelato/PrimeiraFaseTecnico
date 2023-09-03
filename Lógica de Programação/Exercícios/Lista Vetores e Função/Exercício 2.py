nomes = []
auxvetor = []

def main():
    for i in range(3):
        nomes.append(input("Digite um nome: "))
    num_caracter = int(input("Digite o numero de caracteres desejados: "))
    for i in range(3):
        if(num_caracter <= len(nomes[i])):
            auxvetor.append(nomes[i])
            
    print(auxvetor)
                
        
            
main()