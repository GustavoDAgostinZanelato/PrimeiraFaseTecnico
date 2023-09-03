def rendimento(nome_cliente,tipo_investimento,valor):
    
    if(tipo_investimento == 1):
        valor_corrigido = (valor * 1.05)
        
    elif(tipo_investimento == 2):
        valor_corrigido = (valor * 1.08)
        
    elif(tipo_investimento == 3):
        valor_corrigido = (valor * 1.1)
        
    else:
        return(print("ERRO. Informe um investimento válido"))
        
    print("O investimento em", tipo_investimento, "será de", valor_corrigido)

nome_cliente = str(input("Insira o seu nome: "))
valor = float(input("Indique o valor a ser investido: "))
tipo_investimento = int(input("Insira o investimento desejado: \n1-Poupança \n2-Renda Fixa \n3-Fundos de Investimentos "))

rendimento(nome_cliente,tipo_investimento,valor)
