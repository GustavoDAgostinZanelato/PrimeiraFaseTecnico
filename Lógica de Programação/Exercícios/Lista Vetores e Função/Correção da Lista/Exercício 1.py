numero = []

def verifica(n):
    achou = False
    for i in range (len(numero)):
        if n == numero[i]:
            achou = True
            break
    if (achou == True):
        print("Número Repetido!!")
    return achou

def main():
    for i in range (10):
        while True:
            aux_num = int(input(f"Digite o {1+i}º número: "))
            achou = verifica(aux_num)
            if (achou == False):
                numero.append(aux_num)
                break
    print(numero)

main()