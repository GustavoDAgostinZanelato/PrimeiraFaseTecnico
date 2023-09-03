notas_alunos = []
soma_notas = 0

for i in range (15):
    nota = float(input(f"Digite a nota da prova do {i+1}º aluno: "))
    notas_alunos.append(nota)
    soma_notas = soma_notas + nota
    
media = soma_notas/15

print("A média da nota da sala foi de:", media)
    
    