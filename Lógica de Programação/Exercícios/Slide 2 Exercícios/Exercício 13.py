qtd_sal_menor_1500 = 0
qtd_sal_entre_1500_3000 = 0
qtd_sal_maior_3000 = 0

for i in range(100):
    nome = input(f"Informe o nome do {i + 1}º funcionário: ")
    salario = float(input(f"Informe o salário do {i + 1}º funcionário: "))

    if salario < 1500:
        qtd_sal_menor_1500 += 1
    elif salario < 3000:
        qtd_sal_entre_1500_3000 += 1
    else:
        qtd_sal_maior_3000 += 1

print(f"Quantidade de funcionários em cada faixa salarial:")
print(f"Salário menor que R$ 1.500,00: {qtd_sal_menor_1500}")
print(f"Salário maior que R$ 1.500,00 e menor que R$ 3.000,00: {qtd_sal_entre_1500_3000}")
print(f"Salário maior que R$ 3.000,00: {qtd_sal_maior_3000}")
