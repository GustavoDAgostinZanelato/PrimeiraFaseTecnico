#área de seleção das variáveis:
maior = maiorpeixe = 0
pesopeixe = 0

npeixes = int(input("Quantos peixes você pegou? "))

#Coletando dados:
for i in range(npeixes):
    nome = str(input("Qual a espécie do seu peixe: "))
    quilo = float(input("Qual o peso do peixe: "))

    pesopeixe = pesopeixe + quilo

    if(i == 0):
        maiorpeixe = quilo
        maior = nome

    else:
        if(quilo > maiorpeixe):
            maiorpeixe = quilo
            maior = nome

#Texto com as respostas:
print("A soma dos pesos dos peixes pegos foram: ", pesopeixe)
print("Seu maior peixe foi: ",maior, maiorpeixe, "kg")
print("A média do peso dos seus peixes foram: ", pesopeixe/npeixes)