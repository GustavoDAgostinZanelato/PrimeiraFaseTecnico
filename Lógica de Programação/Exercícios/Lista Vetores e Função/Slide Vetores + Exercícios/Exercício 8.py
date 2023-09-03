num_int = (2, 4, 6, 8, 10, 12)

print(num_int)

escolha_num = int(input("Escolha uma das casas da sequência: "))

print("O número presente nessa casa é o:", num_int[escolha_num])
print("A sequência tem ao todo", len(num_int), "valores inteiros diferentes")