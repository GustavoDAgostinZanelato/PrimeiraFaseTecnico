tempo_mergulhos = []
contador_mergulhos = 0

def cadastrar_mergulho():
    global contador_mergulhos
    
    if(contador_mergulhos < 50):
        contador_mergulhos = contador_mergulhos + 1 
        tempo = int(input("Digite o tempo do seu mergulho: "))
        tempo_mergulhos.append(tempo)
    else:
        print("Limite de mergulhos atingido!!!")

def registro():
        maior_tempo = 0
        posicao = 0
        for i in range(len(tempo_mergulhos)):
            if(i == 0):
                maior_tempo = maior_tempo
                posicao = i
            else:
                maior_tempo = tempo_mergulhos[i]
                posicao = i + 1 
                
        print("Mergulhos realizados:",tempo_mergulhos)
        print("Seu",posicao,"mergulho foi o mais longo. Você mergulhou por",maior_tempo,"segundos")
    
def main ():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Cadastar Mergulho \n2-Registro \n3- Sair  "))
    
        if(menu == 1):
            cadastrar_mergulho()
        if(menu == 2):
            registro()
        if(menu == 3):
            break

main()