Algoritmo "Exercicio 4"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 
   sl,soma: real
   nome,dp: caracter

Inicio
//coletando dados
            escreva ("qual seu nome: ")
            leia (nome)
            escreva ("qual o seu departamento: " )
            leia (dp)
            escreva ("qual o seu salario: ")
            leia (sl)
            
            se(dp = "vendas") então
                 soma := (sl/100)*2 +sl)
                 escreva (soma)
            fimse
            
            se(dp = "produção") então
                 soma := (sl/100)*5 +sl)
                 escreva (soma)
            fimse
            
             se(dp = "compras") então
                 soma := (sl/100)*3 +sl)
                 escreva (soma)
            fimse
            
             se(dp = "almoxarifado") então
                 soma := (sl/100)*4 +sl)
                 escreva (soma)
            fimse
            


Fimalgoritmo