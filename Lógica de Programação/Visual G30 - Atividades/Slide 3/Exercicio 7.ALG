Algoritmo "Exercicio 7"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 
     nome: caracter
     idade: real

Inicio
//coletando dados
            escreva ("qual seu nome: ")
            leia (nome)
            escreva ("qual a sua idade: " )
            leia (idade)
            
//analise dos dados obtidos

          se (idade <= 15) então
             escreva ("não votante")
          fimse
          
          se (idade >= 18) e ( idade <= 65) então
             escreva ("eleitor obrigatório")
          fimse
          
          se (idade = 16) ou (idade = 17) ou (idade > 65) então
             escreva ("voto facultativo")
          fimse

Fimalgoritmo