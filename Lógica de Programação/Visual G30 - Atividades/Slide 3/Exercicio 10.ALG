Algoritmo "Exercicio 10"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2023
Var
// Seção de Declarações das variáveis 
     nome,doup: caracter
     saldo,soma,soma2,saque,deposito: real


Inicio
//coletando dados
            escreva ("qual o seu nome: ")
                    leia (nome)
            escreva ("o saldo da sua conta é de 500 reais")
                    leia (saldo)
            
//analise dos dados obtidos

            escreva ("solicite a operação desejada, deposito ou saque: ")
                    leia(doup)
       
       se (doup = "saque") entao
                escreva ("qual o valor do seu saque: ")
                        leia (saque)
                        soma := ((500) - (saque))
                             escreva ("seu saldo é de", soma)
       fimse
       
       se (doup = "deposito") então
                escreva ("qual é o valor do seu deposito: ")
                        leia (deposito)
                        soma2 := ((500) + (deposito))
                              escreva ("seu saldo é de", soma2)
       fimse
       
Fimalgoritmo