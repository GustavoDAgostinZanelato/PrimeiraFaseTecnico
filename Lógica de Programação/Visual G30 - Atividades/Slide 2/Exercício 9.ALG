Algoritmo "Exerc�co 9 - Slide 2"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Luciano B. Fernandes
// Descri��o   : Verificar tipode de tir�ngulos
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
      se ((lA + lb > lc) e (la + lc > lb) e (lb + lc > la)) ent�o
         se (la=lb) e (la=lc) ent�o
            escreva ("Tri�ngulo Equil�tero")
         senao
              se (la<>lb) e (la<>lc) e (lc<>lb) ent�o
                 escreva ("Tri�ngulo Escaleno")
              sen�o
                   escreva ("Triangulo Is�celes")
                   fimse
              fimse
         sen�o
              escreva ("Medidas n�o formam um tri�ngulo")
         fimse
         fimalgoritmo
