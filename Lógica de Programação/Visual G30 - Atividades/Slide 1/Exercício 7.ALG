Algoritmo "C�lculo de IMC"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Se��o de Declara��es das vari�veis 
    nome: caracter
    idade,peso,atura,massa,altura: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
     escreva ("qual o seu nome: ")
     leia (nome)
     escreva ("qual a sua idade: ")
     leia (idade)
     escreva ("qual o seu peso: ")
     leia (peso)
     escreva ("qual � a sua altura: ")
     leia (altura)
     massa := peso/ (altura*altura)
     escreva ("seu IMC � de: ",massa)

Fimalgoritmo