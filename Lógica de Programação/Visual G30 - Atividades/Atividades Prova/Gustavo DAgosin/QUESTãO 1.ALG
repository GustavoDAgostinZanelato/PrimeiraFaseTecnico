Algoritmo "Quest�o 1"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Luciano B. Fernandes
// Descri��o   : Exerc�cio 1
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Se��o de Declara��es das vari�veis 

   nome: caracter
   idade,soma,soma1,soma2,soma3: real

Inicio
//Coleta dos dados nome e idade dos funcion�rios

          escreval ("Algorito de cadastro ao plano de sa�de")
          escreva("Qual � o seu nome: ")
          leia (nome)
          escreva("Qual � a sua idade: ")
          leia (idade)
          
//C�lculo do valor a ser pego dependendo da idade

               se (idade >= 18) e (idade <=30) ent�o
                  soma := (300*5)/100 + 300
                       escreva ("O total a ser pago � de: ", soma)
               fimse
               
               se (idade >= 31) e (idade <=50) ent�o
                  soma1 := (300*10)/100 + 300
                       escreva ("O total a ser pago � de: ", soma1)
               fimse
               
               se (idade >= 51) e (idade <=60) ent�o
                  soma2 := (300*15)/100 + 300
                       escreva ("O total a ser pago � de: ", soma2)
               fimse
               
               se (idade > 60) ent�o
                  soma3 := (300*20)/100 + 300
                       escreva ("O total a ser pago � de: ", soma3)
               fimse
Fimalgoritmo