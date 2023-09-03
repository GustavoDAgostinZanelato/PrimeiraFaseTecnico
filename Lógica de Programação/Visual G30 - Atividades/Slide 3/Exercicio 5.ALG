Algoritmo "Exercicio 5"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 

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
            
//classificação de acordo com os dados

                se (sexo = "homem") entao
                   soma := ((72.7*altura)-58)
                   escreva("seu peso ideal é: ",soma)
                fimse
                
                 se (sexo = "mulher") entao
                   soma := ((62.1*altura)-44.7)
                   escreva("seu peso ideal é: ", soma)
                fimse


Fimalgoritmo