Algoritmo "Cálculo de IMC"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Seção de Declarações das variáveis 
    nome: caracter
    idade,peso,atura,massa,altura: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
     escreva ("qual o seu nome: ")
     leia (nome)
     escreva ("qual a sua idade: ")
     leia (idade)
     escreva ("qual o seu peso: ")
     leia (peso)
     escreva ("qual é a sua altura: ")
     leia (altura)
     massa := peso/ (altura*altura)
     escreva ("seu IMC é de: ",massa)

Fimalgoritmo