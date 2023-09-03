Algoritmo "Cassificação idade"
//  
//  
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Seção de Declarações das variáveis 
    idade: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
      escreva("qual é a sua idade? ")
      leia (idade)
      se (idade=0) e (idade<=10) então
      escreva ("infantil")
      fimse
      se (idade>=11) e (idade<=17) então
      escreva ("juvenil")
      fimse
      se (idade>=18) e (idade<=30) então
      escreva ("adulto)
      fimse
      se (idade>=30) e (idade<=60) então
      escreva ("senior")
      fimse
Fimalgoritmo