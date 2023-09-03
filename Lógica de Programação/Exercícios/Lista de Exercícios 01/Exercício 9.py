nome = str(input("Escreva seu nome: "))
saldo = float(input("Escreva o saldo da sua conta: "))

if saldo > 0 and saldo < 2001:
    print ("Não possui saldo para crédito")

if saldo > 2001 and saldo < 4001:
    print ("O valor do crédito é 5% do saldo médio", (saldo + 5)/100 + saldo)

if saldo > 4001 and saldo < 6000:
    print ("O valor do crédito é 10% do saldo médio", (saldo + 10)/100 + saldo)

if saldo > 6000:
    print ("O valor do crédito é 5% do saldo médio", (saldo + 15)/100 + saldo)



