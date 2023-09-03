contador = 0
paisa = float(input("Informe a população do país A: "))
paisb = float(input("Informe a população do país B: "))
crescimentoa = float(input("Informe o crescimento de A: "))
crescimentob = float(input("Informe o crescimento de B: "))

while(paisa < paisb):

    paisa = paisa * crescimentoa
    paisb = paisb * crescimentob
    contador = contador + 1

print("serão nescessários", contador, "anos para a população de ambos os países seja igual")
