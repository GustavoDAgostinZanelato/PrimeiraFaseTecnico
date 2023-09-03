
while True:

    nome = str(input("Digite sue nome: "))
    senha = input("Digite sua senha: ")

    if nome == senha:
        print("ERRO. Sua senha não pode ser seu nome. Tente Novamente")

    else:
        print("Seu nome registrado foi", nome, "sua senha é ***********")