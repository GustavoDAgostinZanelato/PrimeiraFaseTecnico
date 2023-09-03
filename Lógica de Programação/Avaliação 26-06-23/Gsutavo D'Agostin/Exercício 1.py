#Aluno: Gustavo D'Agostin Zanelato - Matrícula: 50390

#definindo os vetores:
nome = []
nome_bercario = []
bercario = []
edu_infantil = []
fundamental1 = []
fundamental2 = []
contador = 0


#cadastro dos alunos
def cadastro_alunos():
    global contador

    if (contador >= 500): #limite de 500 alunos
        print("Limite de alumos atingido!!!")
        main()

    aux_nome = str(input("Qual o nome do aluno: "))
    nome.append(aux_nome)

    aux_idade = int(input("Qual a idade do aluno: "))

    #a depender da idade, o aluno estará e uma classe diferente
    while True:
        if (aux_idade >= 0) and (aux_idade <= 2):
            print("Berçário")
            nome_bercario.append(aux_nome)
            bercario.append(aux_idade)
            contador = contador + 1
            break

        elif (aux_idade >= 3) and (aux_idade <= 6):
            print("Educação Infantil")
            edu_infantil.append(aux_idade)
            contador = contador + 1
            break

        elif (aux_idade >= 7) and (aux_idade <= 10):
            print("Fundamental 1")
            fundamental1.append(aux_idade)
            contador = contador + 1
            break

        elif (aux_idade >= 11) and (aux_idade <= 15):
            print("Fundamental 2")
            fundamental2.append(aux_idade)
            contador = contador + 1
            break

def alunos_cadastrados():
    while True:

        menu = int(input("Como deseja proseguir: \n1-Mostrar todos os alunos de cada nível \n2-Exibir alunos do Berçário  "))

        #indica a qtd de alunos em cada classe
        if (menu == 1):
            print("Quantidade de alunos no BERÇÁRIO:",len(bercario),"\nQuantidade de alunos na Educação Infantil:",len(edu_infantil),"\nQuantidade de alunos no Fundamental 1:",len(fundamental1),"\nQuantidade de alunos no Fundametal 2:",len(fundamental2))
            main()

        #indica a qtd de alunos somente no berçário
        if (menu == 2):
            print("Segue a lista dos alunos cadastrados no berçário:",nome_bercario)
            main()

#def para um menu onde cada opção levará a um def diferente
def main ():
    while True:

        menu = int(input("Como deseja proseguir: \n1-Cadastar Alunos \n2-Mostrar Alunos Cadastrados \n3-Sair  "))

        if(menu == 1 ):
            cadastro_alunos()
        if(menu == 2):
            alunos_cadastrados()
        if(menu == 3):
            break #usado para parar o código

main()
