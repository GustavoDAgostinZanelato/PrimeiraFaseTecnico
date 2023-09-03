Algoritmo "Exercicio 6"
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
            
//analise dos dados obtidos

            
            se(dp = "departamento 1") então
                 escreva ("departmento financeiro")
            fimse
            
            se(dp = "departamento 2") então
                 escreva ("departamento contabilidade")
            fimse
            
             se(dp = "departamento 3") então
                 escreva ("dapartamento de compras")
            fimse
            
             se(dp = "departamento 4") então
                 escreva ("departamento de vendas")
                 senao escreva("departamento inválido")
            fimse


Fimalgoritmo