#Coletando dados:
nclientes = int(input("Quantos clientes sua agência possui: "))

for i in range (nclientes):
    nome = str(input("Qual o seu nome: "))
    investimento = str(input("P- Poupança \nRF- Renda Fixa \nFI- Fundos Investimentos \nQual o investimento desejado: "))
    valor = float(input("Qual quantia você deseja investir: "))

#Ajuste do valor a depender od investimento:
    if (investimento == "P"):
        valor = (valor * 0.05) + valor

    elif (investimento == "RF"):
        valor = (valor * 0.08) + valor

    elif (investimento == "FI"):
        valor = (valor * 0.1) + valor

# Texto com a resposta:
    print("O valor corrigido do seu investimento é: ", valor)