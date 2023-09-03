codigo = []
nome = []
salario = []
setor = [] 
contador = 0


def cadastar_funcionario():
    global contador
    
    if(contador == 50):
        print("limite de funcionarios atingido")
        main()
            
    aux_codigo = int(input("Digite seu código de funcionario: "))
    codigo.append(aux_codigo)
    
    aux_nome = str(input("Digite seu nome: "))
    nome.append(aux_nome)
    
    aux_salario = float(input("Digite o seu salário: "))
    salario.append(aux_salario)
    
    while True:
        aux_setor = str(input("Digite seu setor (producao, PCP, adm ou TI): "))
        if(aux_setor != "producao") and (aux_setor != "PCP") and (aux_setor != "adm") and (aux_setor != "TI"):
            print("Digite um setor válido")
        else:
            setor.append(aux_setor)
            contador += 1
            break
    
    
def mostrar_funcionarios():
    
    if(len(nome) == 0):
        print("Nenhum funcionário cadastrado no sistema")
        
    menu = int(input("Como deseja proseguir: \n1-Mostrar dados apenas um funcionario \n2-Mostrar todos os dados  "))
    
    if(menu == 1):
        numero = int (input("Indique qual funcionario vc deseja saber os dados: "))
        print(codigo[numero],nome[numero],salario[numero],setor[numero])
    
    if(menu == 2):
        print(codigo)
        print(nome)
        print(salario)
        print(setor)
    
    
def main ():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Cadastrar funcionario \n2-Mostar funcionarios e seus dados \n3-Sair  "))
    
        if(menu == 1):
            cadastar_funcionario()
        if(menu == 2):
            mostrar_funcionarios()
        if(menu == 3):
            break
    
main()