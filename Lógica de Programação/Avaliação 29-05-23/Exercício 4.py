#Gustavo D'Agostin Zanelato - Matrícula: 50390

#def para o cálculo do salário líquido:
def calculo_salario(cargo,salario):
    if(cargo == 1):
        return (salario * 1.05)

    elif(cargo == 2):
        return (salario * 1.08)

    elif(cargo == 3):
        return (salario * 1.03)

#Coletando dados para a execução do programa:
nome = str(input("Qual o seu nome: "))
cargo = int(input("Informe seu cargo na empresa \n1-Analista \n2-Programador \n3-Outro "))
salario = float(input("Insira o seu salário: "))

#Atribuindo valores ao def:
calculo_salario(cargo,salario)

#Resultado do programa:
resultado = calculo_salario(cargo,salario)
if resultado:
    print("Seu salário líquido final,",nome,",é de: ",resultado)