port = []
ingl = []
def cadPalavras():
    for i in range(10):
        port.append(input("palavra em português: "))
        ingl.append(input("palavra em ingles: "))

def listaPalavras():
    auxpalavra = input("palavra em portugês a procurar: ")
    achou = False
    for i in range(10):
        if (auxpalavra==port[i]):
            print("Palavra em inglês",ingl[i])
            achou = True
            break
    if (achou == False):
        print("Palavra não encontrada")
def main():
    while True:
        op = int(input("1 - Cadastro de Palavras"+
                       "\n2 - Busca Palavras"+
                       "\n3 - Sair"))
        if (op==1):
            cadPalavras()
        if (op==2):
            listaPalavras()
        if (op==3):
            break
main()