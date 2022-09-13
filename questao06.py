tam = int(input("Digite o tamanho da lista 1: "))
l1 = []
print("Preencha a lista 1")
for i in range(0, tam):
    n = int(input("Digite um número inteiro "))
    l1.append(n)

tam = int(input("Digite o tamanho da lista 2: "))
l2 = []
print("Preencha a lista 2")
for j in range(0, tam):
    m = int(input("Digite um número inteiro "))
    l2.append(m)

l3 = l1 + l2
print(l3)
l3.sort()
print(l3)
l3.reverse()
print(l3)
