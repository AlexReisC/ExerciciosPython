from random import randint
n = int(input("Digite um número: "))
lista = []

for i in range(0,n):
    lista.append(randint(0, 4))

x = int(input("Número para verificar na lista: "))
if x in lista:
    print(f'{x} está na lista')
else:
    print(f"{x} não está na lista")
