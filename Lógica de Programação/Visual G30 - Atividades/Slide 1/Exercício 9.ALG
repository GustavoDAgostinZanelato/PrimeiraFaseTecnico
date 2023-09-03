Algoritmo "Salario Burto e INSS"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/02/2023
Var
// Seção de Declarações das variáveis 
   nome,gustavo: caracter
   horas,trabalho,soma,soma2: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
     escreva ("seu nome: ")
     leia (nome)
     escreva ("seu número de horas trabalhadas: ")
     leia (horas)
     escreva ("valor da hora trabalhada: ")
     leia (trabalho)
     soma := (horas*trabalho)
     escreva ("seu salário bruto é: ", soma)
     leia (gustavo)
     soma2 := soma - 2 * (soma/100)
     escreva ("seu salário com desconto é de: ", soma2)
     

Fimalgoritmo