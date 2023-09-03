Algoritmo "Exercicio 8"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 
     nome,es,sexo: caracter


Inicio
//coletando dados
            escreva ("qual seu nome: ")
            leia (nome)
            escreva ("qual sua escolaridade: ")
            leia (es)
            escreva ("qual seu sexo: ")
            leia (sexo)
            
//analise dos dados obtidos

          se (es = "EF") então
             escreva ("Ensino Fundamental")
          fimse
          
          se (es = "EM") então
             escreva ("Ensino Médio")
          fimse
          
          se (es = "ET") então
             escreva ("Ensino Técnico")
          fimse
          
          se (es = "ES") então
             escreva ("Ensino Superior")
          fimse

Fimalgoritmo