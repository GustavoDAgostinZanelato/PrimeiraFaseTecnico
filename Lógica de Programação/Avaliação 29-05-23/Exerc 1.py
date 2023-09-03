dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

dia_semana = int(input("Digite o número do dia da semana que você deseja: "))

for i in range(len(dias)):
    if (dia_semana == dias[i]):
        print(i)