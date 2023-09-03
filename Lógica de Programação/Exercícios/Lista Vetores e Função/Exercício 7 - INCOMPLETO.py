codigo = []
peso = []
raca = []

def cadastro_peso_raca():
    while True: 
        aux_codigo = int(input("Digite o codigo do boi:"))
        codigo.append(aux_codigo)
        
        aux_peso = int(input("Digite o peso do boi: "))
        peso.append(aux_peso)
        
        aux_raca = str(input("Digite a raça do boi: "))
        raca.append(aux_raca)
        break

    
  
def mostrar_bois():
    menu = int(input("Como deseja proseguir: \n1-Mostrar todos os bois \n2-Mostrar determinado boi  "))
        
    if(menu == 1):
        print(peso,"/")
        print(raca,"/")
        print(codigo,"/")
            
    if(menu == 2):
        numero = int(input("Qual boi vc deseja saber as info: "))
        print(peso[numero])
        print(raca[numero])
        print(codigo[numero])
        

def peso():
    
    menu = int(input("Como deseja proseguir: \n1-Saber boi mais GORDO \n2-Saber boi mais MAGRO"))
    
    if(menu == 1):
        gordo = 0
        if(gordo > peso):
            gordo = gordo
        elif(gordo < peso):
            gordo = peso
    
    if(menu == 2):
        magro = 0
        if(magro < peso):
            magro = magro
        elif(magro > peso):
            magro = peso
            
def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Cadrasto do PESO e RAÇA dos bois \n2-Mostrar bois cadastrados \n3-Bois gordos e magros \n4-Sair  "))
        
        if(menu == 1):
            cadastro_peso_raca()
        if(menu == 2):
            mostrar_bois()
        if(menu == 3):
            peso()
        if(menu == 4):
            break
main()