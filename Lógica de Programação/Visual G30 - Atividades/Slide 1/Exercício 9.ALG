Algoritmo "Salario Burto e INSS"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Se��o de Declara��es das vari�veis 
   nome,gustavo: caracter
   horas,trabalho,soma,soma2: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
     escreva ("seu nome: ")
     leia (nome)
     escreva ("seu n�mero de horas trabalhadas: ")
     leia (horas)
     escreva ("valor da hora trabalhada: ")
     leia (trabalho)
     soma := (horas*trabalho)
     escreva ("seu sal�rio bruto �: ", soma)
     leia (gustavo)
     soma2 := soma - 2 * (soma/100)
     escreva ("seu sal�rio com desconto � de: ", soma2)
     

Fimalgoritmo