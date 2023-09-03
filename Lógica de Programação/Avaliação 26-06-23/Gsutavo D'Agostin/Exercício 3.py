#Aluno: Gustavo D'Agostin Zanelato - Matrícula: 50390

#definindo os vetores:
nome = []
peso = []
altura = []
imc = []
abaixo = []
normal = []
acima = []
obeso = []

#def para a coleta de dados dos alunos
def dados():
    aux_nome = str(input("Digite o seu nome: "))
    nome.append(aux_nome)

    aux_peso = float(input("Digite seu peso: "))
    peso.append(aux_peso)

    aux_altura = float(input("Digite sua altura: "))
    altura.append(aux_altura)

    aux_imc = (aux_peso / (aux_altura * aux_altura))
    imc.append(aux_imc)


#def para determinar qual o menor vaor do IMC
def valor_imc():
    menor_imc = 0

    for i in range(len(imc)):
        if (i == 0):
            menor_imc = menor_imc

        else:
            menor_imc = imc[i]

    print("O menor imc é", menor_imc,"e pertence ao aluno(a)",nome[i])


    #dependendo do valor do IMC, as pessoas serão divididas em determinados grupos
    if(menor_imc <= 18.5):
        abaixo.append(1)
        print("Abaixo do Peso. Nessa lista temos:",len(abaixo),"pessoas")

    elif (menor_imc > 18.5) and (menor_imc <= 25):
        normal.append(1)
        print("Peso Normal. Nessa lista temos:",len(normal),"pessoas")

    elif (menor_imc > 25) and (menor_imc <= 30):
        acima.append(1)
        print("Acima do Peso. Nessa lista temos:",len(acima),"pessoas")

    elif (menor_imc > 30):
        obeso.append(1)
        print("Obeso.Nessa lsta temos:",len(obeso),"pessoas")


#def para um menu onde cada opção levará a um def diferente
def main():
    while True:
        menu = int(input("Como deseja continuar: \n1-Informe os dados \n2-Valor IMC \n3-Sair  "))

        if(menu == 1):
            dados()
        if(menu == 2):
            valor_imc()
        if(menu == 3):
            break

main()