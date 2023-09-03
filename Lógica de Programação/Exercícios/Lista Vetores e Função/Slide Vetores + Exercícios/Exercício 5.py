numeros_int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30)
qtd_par = 0 
qtd_impar = 0

for num in numeros_int:
    print(num)
    if((num % 2) == 0):
        qtd_par = qtd_par + 1
    else:
        qtd_impar = qtd_impar + 1
        
print("A quantidade de números Pares na lista é de: ", qtd_par)
print("A quantidade de números Ímpares na lista é de: ", qtd_impar)