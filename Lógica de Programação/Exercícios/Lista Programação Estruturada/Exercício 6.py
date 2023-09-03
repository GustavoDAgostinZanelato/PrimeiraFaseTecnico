def calcular_media(notas, letra, media):
    if letra == 'A':
        media_calculada = sum(notas) / len(notas)
    elif letra == 'P':
        pesos = [5, 3, 2]
        soma_ponderada = sum([nota * peso for nota, peso in zip(notas, pesos)])
        soma_pesos = sum(pesos)
        media_calculada = soma_ponderada / soma_pesos
    elif letra == 'H':
        inversos = [1 / nota for nota in notas]
        media_calculada = len(notas) / sum(inversos)
    else:
        print("Letra inválida. Digite 'A' para média aritmética, 'P' para média ponderada ou 'H' para média harmônica.")
        return

    media.append(media_calculada)


# Leitura das notas do aluno
notas_aluno = []
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
    notas_aluno.append(nota)

# Leitura da letra que indica o tipo de média
letra = input("Digite a letra correspondente ao tipo de média (A para média aritmética, P para média ponderada, H para média harmônica): ")

# Lista para armazenar a média calculada
media = []

# Chamada do procedimento para calcular a média
calcular_media(notas_aluno, letra, media)

# Verificação se a letra foi válida e exibição do resultado
if media:
    print(f"A média calculada é: {media[0]:.2f}")
