Algoritmo "Exercicio 6"
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
            
//analise dos dados obtidos

            
            se(dp = "departamento 1") ent�o
                 escreva ("departmento financeiro")
            fimse
            
            se(dp = "departamento 2") ent�o
                 escreva ("departamento contabilidade")
            fimse
            
             se(dp = "departamento 3") ent�o
                 escreva ("dapartamento de compras")
            fimse
            
             se(dp = "departamento 4") ent�o
                 escreva ("departamento de vendas")
                 senao escreva("departamento inv�lido")
            fimse


Fimalgoritmo