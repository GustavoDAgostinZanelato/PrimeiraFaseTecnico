nomes = []
telefones = []
cidades_estados = []

for i in range(50):
    nome = input("Por favor, insira o nome da pessoa #" + str(i + 1) + ": ")
    telefone = input("Por favor, insira o telefone de " + nome + ": ")
    cidade_estado = input("Por favor, insira a cidade e o estado de " + nome + ": ")

    nomes.append(nome)
    telefones.append(telefone)
    cidades_estados.append(cidade_estado)

print("Lista de Pessoas:")
for i in range(50):
    print("Nome: " + nomes[i] + ", Telefone: " + telefones[i] + ", Cidade/Estado: " + cidades_estados[i])
