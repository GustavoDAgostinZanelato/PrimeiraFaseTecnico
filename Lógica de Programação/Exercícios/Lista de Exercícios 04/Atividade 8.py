torcedores_criciuma = 0
torcedores_avai = 0
torcedores_figueirense = 0
torcedores_outros = 0
soma_salario_criciuma = 0

while True:

    clube = int(input("Qual é o clube de preferência? (1-Criciúma, 2-Avaí, 3-Figueirense, 4-Outros): "))
    salario = float(input("Qual é o salário? "))


    if clube == 1:
        torcedores_criciuma += 1
        soma_salario_criciuma += salario
    elif clube == 2:
        torcedores_avai += 1
    elif clube == 3:
        torcedores_figueirense += 1
    elif clube == 4:
        torcedores_outros += 1


    continuar = input("Deseja cadastrar outra pessoa? (s/n) ")
    if continuar.lower() != 's':
        break


if torcedores_criciuma > 0:
    media_salario_criciuma = soma_salario_criciuma / torcedores_criciuma
else:
    media_salario_criciuma = 0


print("Número de torcedores por clube:")
print("Criciúma:", torcedores_criciuma)
print("Avaí:", torcedores_avai)
print("Figueirense:", torcedores_figueirense)
print("Outros:", torcedores_outros)
print("Média salarial dos torcedores do Criciúma:", media_salario_criciuma)
