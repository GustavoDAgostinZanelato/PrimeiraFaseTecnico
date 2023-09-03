valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))
valor3 = float(input("digite o terceiro valor: "))

if valor1 > valor2 > valor3:
    print(valor1, valor2, valor3)

elif valor2 > valor3 > valor1:
    print(valor2, valor3, valor1)

else:
    print(valor3, valor1, valor2)

print("a media entre os valores é: ", (valor1 + valor2 + valor3)/3)