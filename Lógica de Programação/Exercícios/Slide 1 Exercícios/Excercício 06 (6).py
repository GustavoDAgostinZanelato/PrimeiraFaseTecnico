a = float (input("Medida do lado A: "))
b = float (input("Medida do lado B: "))
c = float (input ("Medida do lado C: "))
if (a+b>c) and (a+c>b) and (c+b>c):
    print ("Medida formam um triângulo")
    if (a==b) and (a==c):
        print ("Equilátero")
    elif (a!=b) and (a!=c) and (c!=b):
        print ("Escaleno")
    else:
        print ("Isoceles")
else:
    print ("Medidas não formam triângulo")

