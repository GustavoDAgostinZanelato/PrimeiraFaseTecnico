#Aluno: Gustavo D'Agostin Zanelato - Matrícula: 50390

#definindo os vetores:
nome = []
nome_gerente = []
cargo = []
gerente = []
salario = []
salario_gerente = []
contador = 0


def cadastro():
    global contador

    if (contador >= 300):  # limite de 500 colaboradores
        print("Limite de colaboradores atingido!!!")
        main()

    aux_nome = str(input("Digite o seu nome: "))
    nome.append(aux_nome)


    aux_salario = float(input("Digite o seu salário: "))
    salario.append(aux_salario)

    while True:
        aux_cargo = str(input("Qual o seu cargo (tecnico, auxiliar, gerente ou outro): "))
        if(aux_cargo == "tecnico"):
            cargo.append(aux_cargo)
            aux_salario = aux_salario * 0.15 + aux_salario
            print("Seu novo salário é de:",aux_salario)
            break

        if(aux_cargo == "auxiliar"):
            cargo.append(aux_cargo)
            aux_salario = aux_salario * 0.10 + aux_salario
            print("Seu novo salário é de:",aux_salario)
            break

        if(aux_cargo == "gerente"):
            gerente.append(aux_cargo)
            nome_gerente.append(aux_nome)
            aux_salario = aux_salario * 0.05 + aux_salario
            salario_gerente.append(aux_salario)
            print("Seu novo salário é de:", aux_salario)
            break

        if(aux_cargo == "outro"):
            cargo.append(aux_cargo)
            aux_salario = aux_salario * 0.08 + aux_salario
            print("Seu novo salário é de:", aux_salario)
            break

        else:
            print("Digite novamente")

def sem_criativdade_pra_nome():

    print("Os funcionários presentes no cargo de gerente são:")
    print(nome_gerente)
    for i in range(len(salario_gerente)):
        print("O total da folha de pagamento dos gerentes é de:", salario_gerente)
        main()


#def para um menu onde cada opção levará a um def diferente
def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Cadastrar Funcionário \n2-Exibir Gerentes \n3-Sair "))

        if(menu == 1):
            cadastro()
        if(menu == 2):
            sem_criativdade_pra_nome()
        if(menu == 3):
            break

main()