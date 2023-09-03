n = int(input("Quantas pessoas frequentam a academia? "))

for i in range(n):
    codigo = int(input("Qual o seu codigo: "))
    altura = float(input("Qual a sua altura: "))
    peso = float(input("Qual o seu peso: "))

    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)

mais_alto = codigos[alturas.index(max(alturas))]
mais_baixo = codigos[alturas.index(min(alturas))]
mais_gordo = codigos[pesos.index(max(pesos))]
mais_magro = codigos[pesos.index(min(pesos))]
media_peso = sum(pesos) / n

print(f"O cliente mais alto é o {mais_alto} com {max(alturas):.2f} metros.")
print(f"O cliente mais baixo é o {mais_baixo} com {min(alturas):.2f} metros.")
print(f"O cliente mais gordo é o {mais_gordo} com {max(pesos):.2f} kg.")
print(f"O cliente mais magro é o {mais_magro} com {min(pesos):.2f} kg.")
print(f"A média de peso dos clientes é de {media_peso:.2f} kg.")