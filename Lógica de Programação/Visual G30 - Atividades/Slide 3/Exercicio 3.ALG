Algoritmo "Exercicio 3"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 
   salario, soma: real

Inicio
//coletando dados
    escreva("qual o seu salario? ")
    leia (salario)
//arquivado dados
            se (salario<300) ent�o
            soma := (salario/100)*5 + salario)
            escreva (soma)
            fimse
            
            se (salario>300) e (salario<400) ent�o
            soma := (salario/100)*3 + salario)
            escreva (soma)
            fimse
            
            se (salario>400) ent�o
            soma := (salario/100)*2 + salario)
            escreva (soma)
            fimse
    

Fimalgoritmo