def conversao(hora,minuto):
    newhora = hora
    res = "A.M."
    if (hora >= 13):
        newhora=hora-12
        res = "P.M."
    return str(newhora)+":"+str(minuto)+ " "+res
def main ():
    while True:
        while True:
            hora = int(input("Infome a Hora: "))
            if (hora<0) or (hora>23):
                print("Horário Inválido!")
            else:
                break
        while True:
            minuto = int(input("Informe o Minuto: "))
            if (minuto<0) or (minuto>59):
                print("Minuto Inválido!")
                break
            else:
                hora24 = conversao(hora, minuto)
                print(hora24)
                cont = input("Deseja continuar? ")
                if (cont == "N"):
                    break

main()