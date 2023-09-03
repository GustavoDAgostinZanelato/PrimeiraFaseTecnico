def peso_ideal(nome,sexo,altura):
    
    if(sexo == "M"):
        resultado = print((72.7 * altura) - 58)
        
    elif(sexo == "F"):
        resultado = print((62.1 * altura) - 44.7)
    else:
        return("Sexo não detectado. Insira um sexo válido.")
    
nome = str(input("Informe o seu nome: "))
sexo = str(input("Informe seu sexo, F (Feminino) ou M (Masculino): "))
altura = float(input("Informe sua altura: "))

resultadofinal = peso_ideal(nome,sexo,altura)



