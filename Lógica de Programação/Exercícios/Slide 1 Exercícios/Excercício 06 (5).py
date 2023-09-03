idade = int(input("Digite sua idade: "))
sexo = input("Seu sexo é masculino (M) ou feminino (F): ")
if (idade>=18):
    if (sexo == "M" ):
        print ("É maior de idade")
        print ("Já pode ser preso")

if (idade<18):
    print ("É menor de idade")

