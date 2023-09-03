codigo = []
nome   = []
salario= []
setor  = []
i = -1
def cadFuncionario():
    global i
    i = i + 1
    codigo.append(i+1)
    print("Código",codigo[i])
    nome.append(input("Digite seu nome : "))
    salario.append(float(input("Salário : ")))
    while True:
        set = input("Setor (Produção/PCP/Adm/TI"+
                    "\nQual setor : ")
        if (set.upper()!= "PRODUÇÃO") and (set.upper()!="PCP") and (set.upper()!="ADM") and (set.upper()!="TI"):
            print("Setor Inválido")
        else:
            break
    setor.append(set)
def listaFuncionario():
    global i
    if (i==-1):
        print("Nenhum funionárion no sistema")
    else:
        auxsetor = input("Qual o setor a procurar : ")
        achou = False
        for i in range(len(codigo)):
            if (auxsetor==setor[i]):
                print(codigo[i],nome[i],setor[i],salario[i])
                achou==True
        if (achou==False):
            print("Nenhum funcionário encontrado!")
def main():
    while True:
        op = int(input("1 - Cadastro de Funcionários"+
                       "\n2 - Lista Funcionários"+
                       "\n3 - Sair"))
        if (op==1):
            cadFuncionario()
        if (op==2):
            listaFuncionario()
        if (op==3):
            break

main()