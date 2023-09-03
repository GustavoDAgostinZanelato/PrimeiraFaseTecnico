Algoritmo "Questão 4"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : luciano B. Fernandes
// Descrição   : Exercicio 4
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Seção de Declarações das variáveis 
    produto,pagamento: caracter
    quantidade,preco,valor,soma,soma1,soma2: real
Inicio
//Coleta dos dados da compra

     escreva ("Qual é o nome do produto: ")
     leia (produto)
     escreva ("Qual é quantidade que você deseja comprar: ")
     leia (quantidade)
     escreva ("Qual é o preço da sua peça: ")
     leia (preco)
     escreva ("Qual será a forma de pagamento: ")
     leia (pagamento)

//Cálculo valor da compra

     valor := (quantidade * preco)

//Valor a ser pago pela forma de pagamento

     se (pagamento = "a vista") então
        soma := (valor - (valor * 10)/100))
        escreva ("O valor de sua compra foi de: ",soma)
     fimse
     
     se (pagamento = "cartao de credito") então
        soma1 := (valor - (valor * 5)/100))
        escreva ("O valor de sua compra foi de: ",soma1)
     fimse
     
      se (pagamento = "2vezes") então
        escreva ("O valor de sua compra foi de: ",valor)
     fimse
     
      se (pagamento = "3vezes") então
        soma2 := (valor + (valor * 5)/100))
        escreva ("O valor de sua compra foi de: ",soma2)
     fimse
Fimalgoritmo