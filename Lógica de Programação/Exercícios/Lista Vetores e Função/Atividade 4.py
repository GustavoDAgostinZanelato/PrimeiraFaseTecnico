frase = str(input("Digite uma frase: "))
letra = str(input("Digite uma letra a ser encontrada na frase digitada: "))

qtd_caracters = len(frase)
qtd_letra = frase.count(letra)

print(frase)
print("A frase possui",qtd_caracters,"caracters")
print("A letra",letra,"apareceu",qtd_letra,"vezes na frase")