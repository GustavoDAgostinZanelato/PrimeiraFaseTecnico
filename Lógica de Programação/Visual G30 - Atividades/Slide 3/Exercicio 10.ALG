Algoritmo "Exercicio 10"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Se��o de Declara��es das vari�veis 
     nome,doup: caracter
     saldo,soma,soma2,saque,deposito: real


Inicio
//coletando dados
            escreva ("qual o seu nome: ")
                    leia (nome)
            escreva ("o saldo da sua conta � de 500 reais")
                    leia (saldo)
            
//analise dos dados obtidos

            escreva ("solicite a opera��o desejada, deposito ou saque: ")
                    leia(doup)
       
       se (doup = "saque") entao
                escreva ("qual o valor do seu saque: ")
                        leia (saque)
                        soma := ((500) - (saque))
                             escreva ("seu saldo � de", soma)
       fimse
       
       se (doup = "deposito") ent�o
                escreva ("qual � o valor do seu deposito: ")
                        leia (deposito)
                        soma2 := ((500) + (deposito))
                              escreva ("seu saldo � de", soma2)
       fimse
       
Fimalgoritmo