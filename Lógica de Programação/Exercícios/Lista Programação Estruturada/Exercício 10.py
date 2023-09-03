def verificacao_media(media):
    
    if(media >= 0) and (media <= 4.9):
        return "D"
    
    elif(media >= 5) and (media <= 6.9):
        return "C"
        
    elif(media >= 7) and (media <= 8.9):
        return "B"
        
    elif(media >= 9) and (media <=10):
        return "A"
    
    else:
        return "Conceito Inválido"

media = float(input("Digite a média final do aluno: "))
verificacao_media(media)

resultado = verificacao_media(media)

if resultado:
    print("A média é verificada como: ",resultado)