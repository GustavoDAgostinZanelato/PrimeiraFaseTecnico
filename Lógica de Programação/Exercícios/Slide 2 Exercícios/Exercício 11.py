count_arquitetura = 0
count_farmacia = 0
count_medicina = 0
count_odontologia = 0

for i in range(100):
    nome = input("Por favor, insira o nome do aluno #" + str(i + 1) + ": ")
    curso = input("Por favor, insira o curso de " + nome + ": ")

    if curso.lower() == "arquitetura":
        count_arquitetura += 1
    elif curso.lower() == "farmácia":
        count_farmacia += 1
    elif curso.lower() == "medicina":
        count_medicina += 1
    elif curso.lower() == "odontologia":
        count_odontologia += 1

print("Resultado:")
print(str(count_arquitetura) + " alunos estão no curso de Arquitetura")
print(str(count_farmacia) + " alunos estão no curso de Farmácia")
print(str(count_medicina) + " alunos estão no curso de Medicina")
print(str(count_odontologia) + " alunos estão no curso de Odontologia")
