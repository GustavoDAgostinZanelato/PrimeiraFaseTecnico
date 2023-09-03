Algoritmo "Algoritmo Classificaçaõ Idade 2"
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
      se (idade=0) e (idade<=3) então
      escreva ("bebe")
      fimse
      se (idade>=4) e (idade<=11) então
      escreva ("criança")
      fimse
      se (idade>=12) e (idade<=17) então
      escreva ("adolescente")
      fimse
      se (idade>=18) e (idade<=60) então
      escreva ("adulto")
      fimse
      se (idade>=61) e (idade<=99) então
      escreva ("3 idade")
      fimse

Fimalgoritmo