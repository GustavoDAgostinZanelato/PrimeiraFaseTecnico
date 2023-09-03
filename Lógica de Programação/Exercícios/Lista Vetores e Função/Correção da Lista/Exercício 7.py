bois = []

def cadastrar_boi():
    if len(bois) >= 100:
        print("Limite máximo de bois atingido.")
        return
    
    identificador = len(bois) + 1
    peso = float(input("Digite o peso do boi de identificador {}: ".format(identificador)))
    raca = input("Digite a raça do boi de identificador {}: ".format(identificador))
    
    bois.append((identificador, peso, raca))
    print("Boi cadastrado com sucesso.")

def listar_bois():
    if len(bois) == 0:
        print("Nenhum boi cadastrado.")
        return
    
    for boi in bois:
        identificador, peso, raca = boi
        print("Identificador: {}, Peso: {:.2f} kg, Raça: {}".format(identificador, peso, raca))

def encontrar_boi_mais_gordo():
    if len(bois) == 0:
        print("Nenhum boi cadastrado.")
        return
    
    boi_mais_gordo = min(bois, key=lambda x: (x[1], -x[0]))
    identificador, peso, raca = boi_mais_gordo
    print("Boi mais gordo: Identificador: {}, Peso: {:.2f} kg, Raça: {}".format(identificador, peso, raca))

def encontrar_boi_mais_magro():
    if len(bois) == 0:
        print("Nenhum boi cadastrado.")
        return
    
    boi_mais_magro = max(bois, key=lambda x: (x[1], x[0]))
    identificador, peso, raca = boi_mais_magro
    print("Boi mais magro: Identificador: {}, Peso: {:.2f} kg, Raça: {}".format(identificador, peso, raca))

while True:
    print("\nMenu:")
    print("1. Cadastrar boi")
    print("2. Listar bois")
    print("3. Encontrar boi mais gordo")
    print("4. Encontrar boi mais magro")
    print("5. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_boi()
    elif opcao == 2:
        listar_bois()
    elif opcao == 3:
        encontrar_boi_mais_gordo()
    elif opcao == 4:
        encontrar_boi_mais_magro()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Digite novamente.")
