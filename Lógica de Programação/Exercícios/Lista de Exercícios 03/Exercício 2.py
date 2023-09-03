tas = tpr = tgp = 0
n = int(input("Quantos funcionários trabalham na empresa: "))

for i in range(n):
    nome = input("Qual o nome: ")
    salario = int(input("Qual o salario: "))
    cargo = input("\nAS - Analista de Sistemas"
                  "\nPR - Programador"
                  "\nGP - Gerente de Projetos"
                  "\nQual é a sua função: ")

    if (cargo == "AS"):
        tas = tas + salario

    elif (cargo == "PR"):
        tpr = tpr + salario

    elif (cargo == "GP"):
        tgp = tgp + salario

print("Total salário Programador: ", tpr,
      "\n Total salário Analista de Sistemas: ", tas,
      "\n Total salário Gerente de Projetos: ", tgp,
      "\nTotal Geral dos Salários: ", (tas + tpr + tgp))