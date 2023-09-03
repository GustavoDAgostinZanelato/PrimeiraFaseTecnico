adm_count = 0
dir_count = 0
cex_count = 0

for i in range(20):
    nome = input("Por favor, insira o nome do aluno #" + str(i + 1) + ": ")
    sigla = input("Por favor, insira a sigla do curso de " + nome + " (ADM, DIR ou CEX): ")

    if sigla == "ADM":
        adm_count += 1
    elif sigla == "DIR":
        dir_count += 1
    elif sigla == "CEX":
        cex_count += 1
    else:
        print("Sigla de curso inválida para " + nome)

print("Resultado:")
print(str(adm_count) + " alunos são de Administração (ADM)")
print(str(dir_count) + " alunos são de Direito (DIR)")
print(str(cex_count) + " alunos são de Comércio Exterior (CEX)")
