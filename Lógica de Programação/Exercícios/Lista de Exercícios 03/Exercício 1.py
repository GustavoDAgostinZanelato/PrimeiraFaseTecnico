nf = nm = nt = gr = 0
curso = 0
naluno = int(input("Número de alunos: "))
for i in range(naluno):
    nome = input("Nome Aluno: ")
    curso = int(input("1 - Ensino Fundamental"
                  "\n 2 - Ensino Médio"
                  "\n 3 - Esino Técnico"
                  "\n Qual a sua formação? "))
if (curso == 1):
    nf=nf+1
elif (curso == 2):
    nm=nm+1
elif (curso == 3):
    nt=nt+1
else:
    gr=gr+1

print("Ensino Fudamental: ", nf,
      "\nEnsino Médio: ", nm,
      "\nEnsino Técnico: ", nt,
      "\nGraduação: ", gr)
