Algoritmo "Quest�o 3"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : luciano B. Fernandes
// Descri��o   : Exercicio 3
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Se��o de Declara��es das vari�veis 
    nome: caracter
    peso,atura,imc,altura: real

Inicio
//Coleta dos dados nome, altura e peso

     escreva ("qual o seu nome: ")
     leia (nome)
     escreva ("qual o seu peso: ")
     leia (peso)
     escreva ("qual � a sua altura: ")
     leia (altura)

//F�rmula do IMC

          imc := peso/(altura*altura)

//Resultado do IMC

            se (imc  < 18) entao
               escreva ("Abaixo do peso")
            fimse

            se (imc >= 18) e (imc <= 25) ent�o
               escreva ("Peso normal")
            fimse

            se (imc > 25) e (imc <=30) entao
               escreva ("Acima do peso")
            fimse

            se (imc > 30) ent�o
               escreva ("Obeso")
            fimse

Fimalgoritmo