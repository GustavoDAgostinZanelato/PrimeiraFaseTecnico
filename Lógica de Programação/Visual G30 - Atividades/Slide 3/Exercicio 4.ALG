Algoritmo "Exercicio 4"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 
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
            
            se(dp = "vendas") ent�o
                 soma := (sl/100)*2 +sl)
                 escreva (soma)
            fimse
            
            se(dp = "produ��o") ent�o
                 soma := (sl/100)*5 +sl)
                 escreva (soma)
            fimse
            
             se(dp = "compras") ent�o
                 soma := (sl/100)*3 +sl)
                 escreva (soma)
            fimse
            
             se(dp = "almoxarifado") ent�o
                 soma := (sl/100)*4 +sl)
                 escreva (soma)
            fimse
            


Fimalgoritmo