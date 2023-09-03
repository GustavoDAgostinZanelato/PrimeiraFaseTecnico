nomes = []
sexos = []
cargos = []
setores = []
salarios = []

for i in range(10):
    nome = input("Por favor, insira o nome do funcionário #" + str(i + 1) + ": ")
    sexo = input("Por favor, insira o sexo de " + nome + ": ")
    cargo = input("Por favor, insira o cargo de " + nome + ": ")
    setor = input("Por favor, insira o setor de " + nome + ": ")
    salario = input("Por favor, insira o salário de " + nome + ": ")

    nomes.append(nome)
    sexos.append(sexo)
    cargos.append(cargo)
    setores.append(setor)
    salarios.append(salario)

print("Lista de Funcionários:")
for i in range(10):
    print("Nome: " + nomes[i] + ", Sexo: " + sexos[i] + ", Cargo: " + cargos[i] + ", Setor: " + setores[
        i] + ", Salário: " + salarios[i])
