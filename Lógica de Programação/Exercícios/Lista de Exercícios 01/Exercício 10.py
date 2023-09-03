salario = float(input("Qual o seu salário: "))
produto = str(input("qual produto vc vendeu (A, B ou C): "))
quantidade = int(input("Quantos do produto vc vendeu: "))

if produto == ('A'):
    print("seu novo salário é: ", (salario + 5)/100 + salario)
    print("vc vendeu do produto A", 5 * quantidade)

elif produto == ('B'):
    print("seu novo salário é: ", (salario + 10)/100 + salario)
    print("vc vendeu, em reais, do produto B", 10 * quantidade)

else:
    print("seu novo salário é: ", (salario + 5)/100 + salario)
    print("vc vendeu do produto C", 15 * quantidade)
