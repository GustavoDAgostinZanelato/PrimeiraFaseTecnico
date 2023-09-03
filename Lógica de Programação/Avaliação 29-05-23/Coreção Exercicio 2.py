def principal():
    totalh = totalidadeh = totalm = totalidadem = 0
    while True:
        nome = input(print('digite o nome do entrevistado :'))
        idade = int(input('digite a sua idade :'))
        sexo = input('sexo (M/F) :')
        cat = input('deseja entrevistar outra pessoa se nao (n) :')
        if (cat == 'n') or (cat == 'N'):
            break
        if (sexo == 'M') or (sexo == 'm'):
            totalh += 1
            totalidadeh += idade
        else:
            total += 1
            totaldem += idade
    mediah = 0
    mediam = 0
    if (totalh > 0):
        maediah = totalidadeh / totalh
    if (totalm > 0):
        mediam = totalidaedem / totalm

    print('media de idade dos homens', mediah)
    print('media de idade das mulheres', mediam)


principal()