mergulho = []
i = -1

def cadMergulho():
    global i
    if (i<=48):
        i = i + i
        tempo = int(input("Tempo de Mergulho: "))
        mergulho.append(tempo)
    else:
        print("Número máximo de mergulhos no sistema: ")

def listaMergulho():
    maior = 0
    posicao = 0
    for i in range(len(mergulho)):
        if (i==0):
            maior = mergulho[i]
            posicao = i
        else:
            if(maior < mergulho[i]):
                maior = mergulho[i]
                posicao = i
    print("O maior tempo de mergulho foi de:",maior,"segundos")
    print("O",(posicao+1),"° mergulho foi o mais demorado")
        
def main():
    while True:
        op = int(input("1- Cadastro de Mergulho"+"\n2- Verificação de Mergulho"+"\n3- Sair  "))

        if (op==1):
            cadMergulho()
        if(op==2):
            listaMergulho()
        if(op==3):
            break

main()
    
