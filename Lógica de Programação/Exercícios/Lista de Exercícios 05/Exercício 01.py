def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    maior(a,b,c)

def maior(a,b,c):
    if(a>b) and (a>c):
        print("A é a maior nota")
    elif(b>a) and (b>c):
        print("B é a maior nota")
    else:
        print("C é a maior nota")
main()