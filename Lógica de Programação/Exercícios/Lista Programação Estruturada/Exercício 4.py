def escolaridade(nome,idade):
    if (idade >= 5) and (idade <= 7):
        resultado = "Infantil"
        
    elif (idade >= 7) and (idade <= 15):
        resultado = "Fuldamental"
        
    elif (idade >= 16) and (idade <= 18):
        resultado = "Ensino Médio"
    
    elif (idade > 18):
        resultado = "Graduação"
        
    print("O nível de escolaridade do aluno", nome, "é: ",resultado)

nome = str(input("Indique o seu nome: "))
idade = int(input("Indique a sua idade: "))
escolaridade (nome,idade)

