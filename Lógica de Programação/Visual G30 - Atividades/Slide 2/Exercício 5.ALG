Algoritmo "Algoritmo Classifica�a� Idade 2"
//  
//  
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Se��o de Declara��es das vari�veis 
      idade: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
             escreva("qual � a sua idade? ")
      leia (idade)
      se (idade=0) e (idade<=3) ent�o
      escreva ("bebe")
      fimse
      se (idade>=4) e (idade<=11) ent�o
      escreva ("crian�a")
      fimse
      se (idade>=12) e (idade<=17) ent�o
      escreva ("adolescente")
      fimse
      se (idade>=18) e (idade<=60) ent�o
      escreva ("adulto")
      fimse
      se (idade>=61) e (idade<=99) ent�o
      escreva ("3 idade")
      fimse

Fimalgoritmo