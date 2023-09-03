nomes = []
cargos = []

for i in range(300):
    nome = input(f"Informe o nome do {i + 1}º funcionário: ")
    cargo = input(
        f"Informe o cargo do {i + 1}º funcionário (Engenheiro Mecânico, Engenheiro Elétrico ou Engenheiro Civil): ")

    nomes.append(nome)
    cargos.append(cargo)

qtd_eng_mec = cargos.count("Engenheiro Mecânico")
qtd_eng_eletr = cargos.count("Engenheiro Elétrico")
qtd_eng_civil = cargos.count("Engenheiro Civil")

print(f"Quantidade de funcionários de cada cargo:")
print(f"Engenheiro Mecânico: {qtd_eng_mec}")
print(f"Engenheiro Elétrico: {qtd_eng_eletr}")
print(f"Engenheiro Civil: {qtd_eng_civil}")
