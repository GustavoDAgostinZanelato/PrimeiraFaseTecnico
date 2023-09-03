idade = int(input("Quantos anos você tem? "))
idade2 = int(input("Quantos meses faltam para o seu próximo aniversário? "))

dias = (idade * 365)
meses = (12-idade2)
resultado = print("Você tem", idade, "anos e", meses, " meses de vida. Você já vivieu", dias + meses * 30)