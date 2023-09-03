portugues = []
ingles = []

def palavras():  
    for i in range(2):
        aux_port = str(input("Digite uma palavra em PORTUGUES: "))
        portugues.append(aux_port)
            
        aux_ingles = str(input("Digite a tradução dessa palavra em INGLES: "))
        ingles.append(aux_ingles)
    
def verificador():
    
    palavra = str(input("Escreva a palavra em Portugues que vc deseja saber a tradução em Ingles: "))
    
    for i in range(2):
        if(palavra == portugues[i]):
            print("A tradução de",palavra,"para ingles é",ingles[i])
            print("")

def main():
    while True:
        
        menu = int(input("Como deseja continuar: \n1-Digitar palavras \n2-Saber a Traduçao \n3-Sair  "))
        
        if(menu == 1):
            palavras()
        if(menu == 2):
            verificador()
        if(menu == 3):
            break
        
main()
    
    