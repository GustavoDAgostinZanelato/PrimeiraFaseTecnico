def calculo (raio_esfera):
    
    volume = (4/3 * 3.14 * (raio_esfera * raio_esfera * raio_esfera))
    
    print("O volume da esfera é de", volume)


raio_esfera = float(input("Indique o raio de sua esfera: "))
calculo(raio_esfera)