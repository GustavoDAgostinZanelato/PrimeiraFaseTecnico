Algoritmo "Exercíco 2"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Luciano B. Fernandes
// Descrição   : Verificar tipode de tirângulos
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 13/03/2023
Var
  nome: caracter
  peso: real
Inicio
//nome e peso do lutador
      escreva ("Qual o seu nome: ")
      leia (nome)
      escreva ("Qual o seu peso: ")
      leia (peso)
//categoria de acordo com o peso do lutador

   se(peso>51) e (peso<61) entao
               escreval ("Categoria Super Pena")
   fimse
   
   se(peso>61) e (peso<80) entao
               escreval ("Categoria Pena")
   fimse
   
   se(peso>81) e (peso<100) entao
               escreval ("Categoria Peso Médio")
   fimse
               
   se(peso>101) e (peso<120) entao
                escreval ("Categoria Peso Pesado")
   fimse

fimalgoritmo
