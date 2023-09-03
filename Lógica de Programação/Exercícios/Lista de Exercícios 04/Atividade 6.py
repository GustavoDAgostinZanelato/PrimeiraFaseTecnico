import random

freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(1000):
    giros = random.randint(1, 6)
    freq[giros] += 1

for num, count in freq.items():
    print("Numero", num, "ocorreu", count, "vezes. Frequencia:", count / 1000)
