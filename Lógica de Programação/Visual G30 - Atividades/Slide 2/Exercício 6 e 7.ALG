Algoritmo "Cassifica��o idade"
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
      se (idade=0) e (idade<=10) ent�o
      escreva ("infantil")
      fimse
      se (idade>=11) e (idade<=17) ent�o
      escreva ("juvenil")
      fimse
      se (idade>=18) e (idade<=30) ent�o
      escreva ("adulto)
      fimse
      se (idade>=30) e (idade<=60) ent�o
      escreva ("senior")
      fimse
Fimalgoritmo