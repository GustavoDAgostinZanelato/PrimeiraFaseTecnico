Algoritmo "Quest�o 2"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Luciano B. Fernandes
// Descri��o   : Exerc�cio 2
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 20/03/2023
Var
// Se��o de Declara��es das vari�veis 

   nome: caracter
   idade,peso: real

Inicio
//Coleta dos dados nome, idade e peso

          escreval ("Algorito de cadastro HEMOSC")
          escreva("Qual � o seu nome: ")
          leia (nome)
          escreva("Qual � a sua idade: ")
          leia (idade)
          escreva("Qual � o seu peso: ")
          leia (peso)
          
//Classifica��o de quem pode ou n�o doar sangue

              se (idade <= 15) ent�o
                 escreva("Apenas pessoas com 16 anos ou mais podem ser doadoras")
              fimse
              
              se (idade = 16) ou (idade = 17) ent�o
                 se (peso >= 50) ent�o
                    escreva ("Voc� nescessita da autoriza��o do seu respons�vel para realizar a doa��o")
                 fimse
              fimse
              
               se (idade >= 18) e (idade <= 69) ent�o
                 se (peso >= 50) ent�o
                    escreva ("Voc� pode doar sangue")
                 fimse
              fimse
              
               se (idade > 69) ent�o
                    escreva ("Idade limite extrapolada, voc� n�o pode doar sangue")
               fimse
               
               se (peso < 50) ent�o
                  escreva ("Voc� n�o possui peso suficiente para ser um doador de sangue")
               fimse
Fimalgoritmo