Algoritmo "Questão 3"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : luciano B. Fernandes
// Descrição   : Exercicio 3
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Seção de Declarações das variáveis 
    nome: caracter
    peso,atura,imc,altura: real

Inicio
//Coleta dos dados nome, altura e peso

     escreva ("qual o seu nome: ")
     leia (nome)
     escreva ("qual o seu peso: ")
     leia (peso)
     escreva ("qual é a sua altura: ")
     leia (altura)

//Fórmula do IMC

          imc := peso/(altura*altura)

//Resultado do IMC

            se (imc  < 18) entao
               escreva ("Abaixo do peso")
            fimse

            se (imc >= 18) e (imc <= 25) então
               escreva ("Peso normal")
            fimse

            se (imc > 25) e (imc <=30) entao
               escreva ("Acima do peso")
            fimse

            se (imc > 30) então
               escreva ("Obeso")
            fimse

Fimalgoritmo