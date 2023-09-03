Candidado1 = Candidado2 = Candidado3 = Candidado4 = 0
votonulo = 0
votobranco = 0
maisvotos = 0

for i in range(4):
    codigo = int(input(
        "1- Candidado 1 \n2- Candidado 2 \n3- Candidado 3 \n4- Candidado 4 \n5- Voto Nulo \n6- Voto em Branco \nQual opção você deseja? "))

    if (codigo == 1):
        Candidado1 = Candidado1 + 1

    elif (codigo == 2):
        Candidado2 = Candidado2 + 1

    elif (codigo == 3):
        Candidado3 = Candidado3 + 1

    elif (codigo == 4):
        Candidado4 = Candidado4 + 1

    elif (codigo == 5):
        votonulo = votonulo + 1

    elif (codigo == 6):
        votobranco = votobranco + 1

    if (i == 0):
        maisvotos = codigo

    else:
        if (maisvotos > codigo):
            maisvotos = codigo

print("Candidado 1 recebeu", Candidado1, "votos."
                                         "\nCandidado 2 recebeu", Candidado2, "votos."
                                                                              "\nCandidado 3 recebeu", Candidado3,
      "votos."
      "\nCandidado 4 recebeu", Candidado4, "votos.")

print("A quanitdade de votos nulos foi de", votonulo, "votos."
                                                      "\nA quantidade  de votos em branco foi de", votobranco, "votos.")

print("O vencedor da eleição foi o candidato", maisvotos)