Algoritmo "Exercicio 8"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 
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

          se (es = "EF") ent�o
             escreva ("Ensino Fundamental")
          fimse
          
          se (es = "EM") ent�o
             escreva ("Ensino M�dio")
          fimse
          
          se (es = "ET") ent�o
             escreva ("Ensino T�cnico")
          fimse
          
          se (es = "ES") ent�o
             escreva ("Ensino Superior")
          fimse

Fimalgoritmo