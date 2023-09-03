Algoritmo "valor da compra"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Seção de Declarações das variáveis 
   a: caracter
   calca, blusa,soma: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
//peça 1= calça peça 2= blusa

  escreva ("o valor do IPI acrecid em cada peça é de 5%")
  leia (A)
  escreva ("quantas calças voce escolheu? ")
  leia (calca)
  escreva ("quantas blusas voc escoheu? ")
  leia (blusa)
  soma := (50*calca) + (40*blusa)*(5/100 + 1)
  escreva ("o valor da sua compra foi: ", soma)
Fimalgoritmo