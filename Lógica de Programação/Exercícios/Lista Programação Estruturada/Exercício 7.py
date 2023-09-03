def verificar(valor):
    
    if(valor > 0):
        resultado = "Verdadeiro"
        
    else:
        resultado = "Falso"
        
    print("O resultado é", resultado)

valor = int(input("Informe um valor inteiro positivo para uma análise de Verdadeiro ou Falso: "))
verificar(valor)
