Algoritmo "Exercíco 9 - Slide 2"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Luciano B. Fernandes
// Descrição   : Verificar tipode de tirângulos
// Autor(a)    : Gustavo D'Agostin Zanelato
// Data atual  : 13/03/2023
Var
   la, lb, lc: real
      

Inicio

      escreva ("Medida do lado A: ")
      leia (la)
      escreva ("Medida do lado B: ")
      Leia (lb)
      escreva ("Medida do lado C: ")
      leia (lc)
      se ((lA + lb > lc) e (la + lc > lb) e (lb + lc > la)) então
         se (la=lb) e (la=lc) então
            escreva ("Triângulo Equilátero")
         senao
              se (la<>lb) e (la<>lc) e (lc<>lb) então
                 escreva ("Triângulo Escaleno")
              senão
                   escreva ("Triangulo Isóceles")
                   fimse
              fimse
         senão
              escreva ("Medidas não formam um triângulo")
         fimse
         fimalgoritmo
