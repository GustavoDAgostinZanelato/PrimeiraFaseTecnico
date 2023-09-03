nomes = []
enderecos = []
cidades = []
estados = []
telefones = []
cursos = []

for i in range(10):
    nome = input("Por favor, insira o nome do aluno #" + str(i + 1) + ": ")
    endereco = input("Por favor, insira o endereço de " + nome + ": ")
    cidade = input("Por favor, insira a cidade de " + nome + ": ")
    estado = input("Por favor, insira o estado de " + nome + ": ")
    telefone = input("Por favor, insira o telefone de " + nome + ": ")
    curso = input("Por favor, insira o curso de " + nome + ": ")

    nomes.append(nome)
    enderecos.append(endereco)
    cidades.append(cidade)
    estados.append(estado)
    telefones.append(telefone)
    cursos.append(curso)

print("Lista de Alunos:")
for i in range(10):
    print("Nome: " + nomes[i] + ", Endereço: " + enderecos[i] + ", Cidade: " + cidades[i] + ", Estado: " + estados[
        i] + ", Telefone: " + telefones[i] + ", Curso: " + cursos[i])
