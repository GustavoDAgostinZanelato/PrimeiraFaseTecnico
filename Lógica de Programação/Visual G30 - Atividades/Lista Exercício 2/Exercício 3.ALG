Algoritmo "reajuste 1%"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2023
Var
// Seção de Declarações das variáveis 
      saldo, soma: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
      escreva ("O saldo da sua conta poupança: ")
      leia (saldo)
      soma := (saldo) - (saldo/100*1)
      escreva ("o saldo da sua conta depois do reajuste de 1% foi de: ", soma)

Fimalgoritmo