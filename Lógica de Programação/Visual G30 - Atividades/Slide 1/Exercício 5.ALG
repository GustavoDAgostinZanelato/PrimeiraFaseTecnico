Algoritmo "Aumento de Salário"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Seção de Declarações das variáveis 
    nome,cargo: caracter
    salario,soma,salario1,salario2: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

   escreva("seu nome: ")
   leia (nome)
   escreva("seu cargo: ")
   leia(cargo)
   escreva("seu salário: ")
   leia (salario1)
   soma := salario1 + 5 * (salario1/100)
   escreva ("seu amento de salario foi de: ",soma)

Fimalgoritmo