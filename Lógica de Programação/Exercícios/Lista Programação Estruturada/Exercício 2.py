def categoria_jogador (nome,idade):
    if (idade >= 5) and (idade <= 10):
        categoria = "Categoria Juvenil"
        
    elif (idade >= 11) and (idade <= 17):
        categoria = "Categoria Júnior"
        
    elif (idade >= 18) and (idade > 35):
        categoria = "Categoria Profissional"
        
    print("O jogador", nome,"está na categoria", categoria)

nome = str(input("Insira o nome do jogador: "))
idade = int(input("Insira a idade do jogador: "))

categoria_jogador(nome,idade)