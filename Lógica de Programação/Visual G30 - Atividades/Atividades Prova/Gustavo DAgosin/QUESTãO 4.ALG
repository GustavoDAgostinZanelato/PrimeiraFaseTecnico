Algoritmo "Quest�o 4"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : luciano B. Fernandes
// Descri��o   : Exercicio 4
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Se��o de Declara��es das vari�veis 
    produto,pagamento: caracter
    quantidade,preco,valor,soma,soma1,soma2: real
Inicio
//Coleta dos dados da compra

     escreva ("Qual � o nome do produto: ")
     leia (produto)
     escreva ("Qual � quantidade que voc� deseja comprar: ")
     leia (quantidade)
     escreva ("Qual � o pre�o da sua pe�a: ")
     leia (preco)
     escreva ("Qual ser� a forma de pagamento: ")
     leia (pagamento)

//C�lculo valor da compra

     valor := (quantidade * preco)

//Valor a ser pago pela forma de pagamento

     se (pagamento = "a vista") ent�o
        soma := (valor - (valor * 10)/100))
        escreva ("O valor de sua compra foi de: ",soma)
     fimse
     
     se (pagamento = "cartao de credito") ent�o
        soma1 := (valor - (valor * 5)/100))
        escreva ("O valor de sua compra foi de: ",soma1)
     fimse
     
      se (pagamento = "2vezes") ent�o
        escreva ("O valor de sua compra foi de: ",valor)
     fimse
     
      se (pagamento = "3vezes") ent�o
        soma2 := (valor + (valor * 5)/100))
        escreva ("O valor de sua compra foi de: ",soma2)
     fimse
Fimalgoritmo