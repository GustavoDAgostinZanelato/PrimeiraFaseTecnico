qtd_aprovados = 0
qtd_reprovados = 0

for i in range(50):
    nome = input(f"Informe o nome do {i + 1}º aluno: ")
    media = float(input(f"Informe a média final do {i + 1}º aluno: "))

    if media >= 6:
        qtd_aprovados += 1
    else:
        qtd_reprovados += 1

print(f"Quantidade de alunos aprovados: {qtd_aprovados}")
print(f"Quantidade de alunos reprovados: {qtd_reprovados}")
