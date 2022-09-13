from random import randint
n = int(input("Digite o tamanho da lista "))
lista = [n]

for i in range(0, len(lista)):
    lista.append(randint(0, n))

for indice in range(0, len(lista)):
    if lista[indice] % 2 == 0:
        del(lista[i])

print(lista)
