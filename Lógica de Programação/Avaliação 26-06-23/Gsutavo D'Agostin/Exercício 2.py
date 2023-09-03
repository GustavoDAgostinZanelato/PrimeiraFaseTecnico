#Aluno: Gustavo D'Agostin Zanelato - Matrícula: 50390

#definindo os vetores:
machado = []
alencar = []
branco = []
contador = 0

#contagem dos votos do candidato Machado
def candidato1 ():

    if (contador >= 10000): #maximo de 10000 votos
        print("Limite de alumos atingido!!!")
        main()

    voto1 = str(input("Comfirmar voto em candidato Machado de Assis (S/N): "))

    if(voto1 == "S"):
        print("Voto Confirmado")
        machado.append(voto1)
    else:
        main()


#contagem dos votos do condidato Assis
def candidato2 ():

    if (contador >= 10000): #maximo de 10000 votos
        print("Limite de votos atingido!!!")
        main()

    voto2 = str(input("Comfirmar voto em candidato José de Alencar (S/N): "))

    if (voto2 == "S"):
        print("Voto Confirmado")
        alencar.append(voto2)
        mais_votado()
    else:
        main()

#Contagem dos votos em branco
def voto_branco ():

    if (contador >= 10000): #maximo de 10000 votos
        print("Limite de votos atingido!!!")
        main()

    branco_voto = str(input("Comfirmar voto em branco (S/N): "))

    if (branco_voto == "S"):
        print("Voto Confirmado")
        branco.append(branco_voto)
        mais_votado()
    else:
        main()


#def para  definir o candidato mais votado
def mais_votado ():

    if(len(machado) > len(alencar)):
        print("O candidato mais votado foi MACHADO DE ASSIS,com: ",len(machado),"votos")
        print("votos em branco:",len(branco))
        print("José de Alencar recebeu: ", len(alencar), "votos")

    elif(len(alencar) > len(machado)):
        print("O candidato mais votado foi JOSÉ DE ALENCAR,com:",len(alencar),"votos")
        print("A quantidade de votos em branco foi de:", len(branco))
        print("Machado de Assis recebeu: ",len(machado),"votos")


#def para um menu onde cada opção levará a um def diferente
def main():
    while True:

        menu = int(input("Como deseja proseguir: \n1-Candidato Machado de Assis \n2-Candidato José de Alencar \n3-Voto em Branco \n4-Resultado \n5-Sair  "))

        if (menu == 1):
            candidato1()
        if (menu == 2):
            candidato2()
        if (menu == 3):
            voto_branco()
        if (menu == 4):
             mais_votado()
        if (menu == 5):
            break

main()

