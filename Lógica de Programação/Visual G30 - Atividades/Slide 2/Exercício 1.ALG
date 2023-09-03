Algoritmo "DigiteSeuNomeeIdade"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Seção de Declarações das variáveis 
     nome,b: caracter
     idade: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
    escreva ("Digite seu nome: ")
    leia (nome)
    escreva ("seu nome é: ",nome)
    leia (b)
    escreva ("qual é a sua idade? ")
    leia (idade)
    se (idade<18) então
    escreva ("você é menor de idade")
    senão
    escreva ("você é maior de idade")
    fimse
    

Fimalgoritmo