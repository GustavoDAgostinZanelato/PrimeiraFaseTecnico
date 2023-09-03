altura = []
sexo = []

altura = float(input("insira sua altura: "))
sexo = input("insiera seu sexo: ")

if sexo == "masculino":
    print("Seu peso ideal é: ", 72.7 * altura - 58)

else:
    print("Seu peso ideal é: ", 62.1 * altura - 44.7)