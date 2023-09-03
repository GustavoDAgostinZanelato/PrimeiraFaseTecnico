import random

def gera ():
    return random.randint(1,6)

def main ():
    vez=um=dois=tres=quatro=cinco=seis=0
    while True:
        numero = gera()
        if (numero == 1): um += 1
        if (numero == 2): dois += 1
        if (numero == 3): tres += 1
        if (numero == 4): quatro += 1
        if (numero == 5): cinco += 1
        if (numero == 6): seis += 1
        vez += 1
        if (vez==50): break
    print("A quatidade de vezes que caiu cada valor no dado após joga-lo 50 vezes foi: \nUm: ", um, "\nDois: ", dois, "\nTrês: ", tres, "\nQuatro: ", quatro, "\nCinco: ", cinco, "\nSeis: ", seis)
main()
