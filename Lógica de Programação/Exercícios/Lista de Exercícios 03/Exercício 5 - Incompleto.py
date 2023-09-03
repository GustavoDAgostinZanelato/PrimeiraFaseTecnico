maisalto = 0
maisgordo = 0
maismagro = altura1 = 0
maisbaixo = peso1 = 0

nclientes = int(input("quantos clientes tem sua academia: "))

for _ in range(nclientes):
    codigo = int(input("qual seu codigo de cliente: "))
    altura = float(input("qual a sua altura: "))
    peso = float(input("qual o seu peso corporal: "))

    if (_ == 0):
        maisalto = altura
        maisbaixo = altura
        maisgordo = peso
        maismagro = peso
        maisalto1 = codigo
        maisbaixo1 = codigo
        maisgordo1 = codigo
        maismagro1 = codigo

    else:
        if (altura > maisalto):
            altura = maisalto
            maisalto1 = codigo

        if (altura < maisbaixo):
            altura1 = maisbaixo
            maisbaixo1 = codigo

        if (peso > maisgordo):
            peso = maisgordo
            maisgordo1 = codigo

        if (peso < maismagro):
            peso1 = maismagro
            maismagro1 = codigo

print("o cliente mais baixo tem: ", altura, "metros", codigo)
print("o cliente mais alto tem: ", altura1, "metros", codigo)
print("o cliente mais magro tem: ", peso, "kg", codigo)
print("o cliente mais gordo tem: ", peso1, "kg", codigo)
print("a media de altura dos clientes é", mediaaltura, "metros")
print("a media de peso dos clientes é", mediapeso, "kg")


