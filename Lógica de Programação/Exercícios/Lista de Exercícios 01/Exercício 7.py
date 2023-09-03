dolar = float(input("escreva a cotação do dolar hoje: "))
real = float(input("escreva a cotação do real hoje: "))

pergunta2 = float(input("digite o valor que deseja saber: "))
pergunta = str(input("dolar ou real? "))

if pergunta == dolar:
    print ("a conversão de real para dolar é: ", dolar * pergunta2)

else:
    print ("a conversão de dolar para real é: ", real * pergunta2)