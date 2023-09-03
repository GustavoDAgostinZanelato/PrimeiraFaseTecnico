mediaveiculos = 0
meior = menor = 0
cidademaior = cidademenor = 0
mediaacidente = 0
totalcidades = 0
for i in range (5):
    codigo = int(input("Código da cidade: "))
    nvp = int(input("Números de veículos: "))
    nat = int(input("Número de acidentes"))
    mediaveiculos = mediaveiculos +nvp
    if(i==0):
        maior = nat
        menor = nat
        cidademaior = codigo
        cidademenor = codigo
    else:
        if nat > maior:
            maior=nat
            cidademaior=codigo
        if nat < menor:
            menor<nat
            cidademenor = codigo

    if (nvp<=2000):
        totalcidades = totalcidades + 1
        mediaacidente = mediaacidente + nat
    print("\n\n", cidademaior, " é a cidade com maior número de acidentes",
          "com ", maior, "número de acidentes")
    print("\n", cidademaior, "é a cidade com maior número de acidentes",
          "com ", menor, "número de acidentes")
    print("\nmMedia de acidentes em cidades com menos de 2000 veículos", (mediaacidente/totalcidades))


            