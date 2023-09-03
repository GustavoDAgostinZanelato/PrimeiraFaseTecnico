codigo = []
nome   = []
peso   = []
status = []
i      = 0

def ListaAlunos():
    if (i==0):
        print("Nenhum Aluno no Sistema !!!")
    else:
        print("Código\tNome\tPeso\tStatus")
        for x in range (len(codigo)):
            if (status[x]=="Ativo"):
                print(codigo[x],nome[x],peso[x],status[x])

def CadAlunos():
    global i
    i += 1
    print("O Código do Aluno vai ser ",i)
    codigo.append(i)
    status.append("Ativo")
    nome.append(input("Digite o nome do aluno : "))
    peso.append(float(input("Digite o peso do aluno :")))

def ListaAlunosPeso():
    if (i==0):
        print("Nenhum Aluno no sistema !!!")
    else:
        auxpeso = float(input("Alunos com peso maior ou igual a : "))
        encontrado = False
        for x in range(len(codigo)):
            if (auxpeso <= peso[x]):
                if (status[x] == "Ativo"):
                    print(codigo[x],nome[x],peso[x],status[x])
                    encontrado = True
        if (encontrado==False):
            print("Nenhum aluno encontrado com essa faixa de peso !!!")

def ExcAluno():
    global i
    if (i==0):
        print("Nenhum Aluno no sistema !!!")
    else:
        auxcodigo = int(input("Código Aluno para Excluir : "))
        encontrado = False
        for x in range(len(codigo)):
            if (auxcodigo == codigo[x]):
                codigo.pop(x)
                nome.pop(x)
                peso.pop(x)
                i -= 1
                encontrado = True
        if (encontrado==False):
            print("Nenhum aluno encontrado para excluir !!!")

def InativarAluno():
    if (i==0):
        print("Nenhum Aluno no sistema !!!")
    else:
        auxcodigo = int(input("Código Aluno para Inativar : "))
        encontrado = False
        for x in range(len(codigo)):
            if (auxcodigo == codigo[x]):
                status[x]  = "Inativar"
                encontrado = True
        if (encontrado==False):
            print("Nenhum aluno encontrado para inativar !!!")

def main():
    while True:
        op = int(input("1 - Cadastro de Aluno"
                       "\n2 - Lista de Alunos"
                       "\n3 - Lista de ALunos por Peso" 
                       "\n4 - Exluir Aluno"
                       "\n5 - Inativar Aluno"
                       "\n6 - Sair "))
        if (op==1):
            CadAlunos()
        if (op==2):
            ListaAlunos()
        if (op==3):
            ListaAlunosPeso()
        if (op==4):
            ExcAluno()
        if (op==5):
            InativarAluno()
        if (op==6):
            break
main()