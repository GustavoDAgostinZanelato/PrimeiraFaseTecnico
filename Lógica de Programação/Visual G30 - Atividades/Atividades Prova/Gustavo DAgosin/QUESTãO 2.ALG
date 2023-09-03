Algoritmo "Questão 2"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Luciano B. Fernandes
// Descrição   : Exercício 2
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Seção de Declarações das variáveis 

   nome: caracter
   idade,peso: real

Inicio
//Coleta dos dados nome, idade e peso

          escreval ("Algorito de cadastro HEMOSC")
          escreva("Qual é o seu nome: ")
          leia (nome)
          escreva("Qual é a sua idade: ")
          leia (idade)
          escreva("Qual é o seu peso: ")
          leia (peso)
          
//Classificação de quem pode ou não doar sangue

              se (idade <= 15) então
                 escreva("Apenas pessoas com 16 anos ou mais podem ser doadoras")
              fimse
              
              se (idade = 16) ou (idade = 17) então
                 se (peso >= 50) então
                    escreva ("Você nescessita da autorização do seu responsável para realizar a doação")
                 fimse
              fimse
              
               se (idade >= 18) e (idade <= 69) então
                 se (peso >= 50) então
                    escreva ("Você pode doar sangue")
                 fimse
              fimse
              
               se (idade > 69) então
                    escreva ("Idade limite extrapolada, você não pode doar sangue")
               fimse
               
               se (peso < 50) então
                  escreva ("Você não possui peso suficiente para ser um doador de sangue")
               fimse
Fimalgoritmo