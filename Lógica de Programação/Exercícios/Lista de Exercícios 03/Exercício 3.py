nmec = nele = ndes = ninf = 0
nalunos = int(input("quantos alunos tem no colegio: "))

for i in range(nalunos):
    nome = str(input("qual o seu nome: "))
    sigla = str(input("INF - Infomática"
                  "\nMEC - Mecatrônica"
                  "\nELE - Eletrônica"
                  "\nDES - Design"
                  "\nQual é a sigla do seu curso: "))

    if sigla == "MEC":
        nmec = nmec + 1

    elif sigla == "ELE":
        nele = nele + 1

    elif sigla == "DES":
        ndes = ndes + 1

    elif sigla == "INF":
        ninf = ninf + 1

print("o numero de alunos na MEC é: " ,nmec,
    "\no numero de alunos na ELE é: ",nele,
    "\no numero de alunos na DES é: ",ndes,
    "\no numero de alunos na INF é: ",ninf)
