Algoritmo "Exercicio 5"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 

   nome, sexo: caracter
   altura,soma: real

Inicio
//coletando dados
            escreva ("qual o seu nome ")
            leia (nome)
            escreva ("qual a sua altura: ")
            leia (altura)
            escreva ("qual o seu sexo: ")
            leia(sexo)
            
//classifica��o de acordo com os dados

                se (sexo = "homem") entao
                   soma := ((72.7*altura)-58)
                   escreva("seu peso ideal �: ",soma)
                fimse
                
                 se (sexo = "mulher") entao
                   soma := ((62.1*altura)-44.7)
                   escreva("seu peso ideal �: ", soma)
                fimse


Fimalgoritmo