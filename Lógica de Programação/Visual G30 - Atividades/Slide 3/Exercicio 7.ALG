Algoritmo "Exercicio 7"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 
     nome: caracter
     idade: real

Inicio
//coletando dados
            escreva ("qual seu nome: ")
            leia (nome)
            escreva ("qual a sua idade: " )
            leia (idade)
            
//analise dos dados obtidos

          se (idade <= 15) ent�o
             escreva ("n�o votante")
          fimse
          
          se (idade >= 18) e ( idade <= 65) ent�o
             escreva ("eleitor obrigat�rio")
          fimse
          
          se (idade = 16) ou (idade = 17) ou (idade > 65) ent�o
             escreva ("voto facultativo")
          fimse

Fimalgoritmo