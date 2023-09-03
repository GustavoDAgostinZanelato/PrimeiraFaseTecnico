Algoritmo "Exercicio 3"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 
   salario, soma: real

Inicio
//coletando dados
    escreva("qual o seu salario? ")
    leia (salario)
//arquivado dados
            se (salario<300) então
            soma := (salario/100)*5 + salario)
            escreva (soma)
            fimse
            
            se (salario>300) e (salario<400) então
            soma := (salario/100)*3 + salario)
            escreva (soma)
            fimse
            
            se (salario>400) então
            soma := (salario/100)*2 + salario)
            escreva (soma)
            fimse
    

Fimalgoritmo