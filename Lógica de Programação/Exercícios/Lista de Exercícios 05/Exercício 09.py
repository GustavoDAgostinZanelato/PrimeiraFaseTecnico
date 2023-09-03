def expressao(n):
    x=1
    while (x<=n):
        res=""
        for i in range(x):
            res+=" "+str(x)
        print(res)
        x += 1

def main():
    n = int(input("Número de vezes: "))
    expressao(n)
main()