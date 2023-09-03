#Gustavo D'Agostin Zanelato - Matrícula: 50390

#def para determinar a categoria do jogador a depender de sua idade:
def categoria_jogador(idade):
    if (idade >= 0) and (idade <= 10):
        return "Categoria Infantil"

    elif (idade >= 11) and (idade <= 17):
        return "Categoria Juvenil"

    elif (idade >= 18) and (idade <= 30):
        return "Categoria Adulto"

    elif (idade <= 31):
        return "Categoria Sênior"

#Etapa de coleta de dados:
nome = str(input("Insira o nome do jogador: "))
idade = int(input("Insira a idade do jogador: "))
categoria_jogador(idade)

#Atribuindo valores ao def:
categoria = categoria_jogador(idade)

#Resultado do programa:
if categoria:
    print("O jogador", nome, "está na", categoria)