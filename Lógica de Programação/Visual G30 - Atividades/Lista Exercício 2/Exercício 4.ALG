Algoritmo "valor da compra"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Se��o de Declara��es das vari�veis 
   a: caracter
   calca, blusa,soma: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
//pe�a 1= cal�a pe�a 2= blusa

  escreva ("o valor do IPI acrecid em cada pe�a � de 5%")
  leia (A)
  escreva ("quantas cal�as voce escolheu? ")
  leia (calca)
  escreva ("quantas blusas voc escoheu? ")
  leia (blusa)
  soma := (50*calca) + (40*blusa)*(5/100 + 1)
  escreva ("o valor da sua compra foi: ", soma)
Fimalgoritmo