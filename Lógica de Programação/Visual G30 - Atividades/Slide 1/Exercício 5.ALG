Algoritmo "Aumento de Sal�rio"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Se��o de Declara��es das vari�veis 
    nome,cargo: caracter
    salario,soma,salario1,salario2: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

   escreva("seu nome: ")
   leia (nome)
   escreva("seu cargo: ")
   leia(cargo)
   escreva("seu sal�rio: ")
   leia (salario1)
   soma := salario1 + 5 * (salario1/100)
   escreva ("seu amento de salario foi de: ",soma)

Fimalgoritmo