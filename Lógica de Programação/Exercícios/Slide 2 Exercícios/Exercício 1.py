people = []

for i in range(10):
    name = input("Insira o nome da pessoa #" + str(i + 1) + ": ")
    age = input("Quantos anos tem " + name + ": ")

    people.append((name, age))

print("Lista de pessoa:")
for person in people:
    print(person[0] + " é " + person[1] + " anos de idade.")
