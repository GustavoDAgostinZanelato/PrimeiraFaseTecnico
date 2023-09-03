rs_count = 0
sc_count = 0
pr_count = 0
sp_count = 0
mg_count = 0

for i in range(50):
    nome = input("Por favor, insira o nome da pessoa #" + str(i + 1) + ": ")
    sigla_estado = input("Por favor, insira a sigla do estado de nascimento de " + nome + " (RS, SC, PR, SP ou MG): ")

    if sigla_estado == "RS":
        rs_count += 1
    elif sigla_estado == "SC":
        sc_count += 1
    elif sigla_estado == "PR":
        pr_count += 1
    elif sigla_estado == "SP":
        sp_count += 1
    elif sigla_estado == "MG":
        mg_count += 1
    else:
        print("Sigla de estado inválida para " + nome)

print("Resultado:")
print(str(rs_count) + " pessoas são do Rio Grande do Sul (RS)")
print(str(sc_count) + " pessoas são de Santa Catarina (SC)")
print(str(pr_count) + " pessoas são do Paraná (PR)")
print(str(sp_count) + " pessoas são de São Paulo (SP)")
print(str(mg_count) + " pessoas são de Minas Gerais (MG)")
