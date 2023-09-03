Algoritmo "Questão 1"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Luciano B. Fernandes
// Descrição   : Exercício 1
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Seção de Declarações das variáveis 

   nome: caracter
   idade,soma,soma1,soma2,soma3: real

Inicio
//Coleta dos dados nome e idade dos funcionários

          escreval ("Algorito de cadastro ao plano de saúde")
          escreva("Qual é o seu nome: ")
          leia (nome)
          escreva("Qual é a sua idade: ")
          leia (idade)
          
//Cálculo do valor a ser pego dependendo da idade

               se (idade >= 18) e (idade <=30) então
                  soma := (300*5)/100 + 300
                       escreva ("O total a ser pago é de: ", soma)
               fimse
               
               se (idade >= 31) e (idade <=50) então
                  soma1 := (300*10)/100 + 300
                       escreva ("O total a ser pago é de: ", soma1)
               fimse
               
               se (idade >= 51) e (idade <=60) então
                  soma2 := (300*15)/100 + 300
                       escreva ("O total a ser pago é de: ", soma2)
               fimse
               
               se (idade > 60) então
                  soma3 := (300*20)/100 + 300
                       escreva ("O total a ser pago é de: ", soma3)
               fimse
Fimalgoritmo