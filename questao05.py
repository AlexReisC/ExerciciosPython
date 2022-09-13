n = int(input("Qual o tamanho da turma: "))
p1 = [n]
p2 = [n]

print("Digite a nota 1 de cada um dos alunos")
soma = 0
soma2 = 0
for i in range(0, n):
    notas1 = float(input(""))
    p1.append(notas1)
    soma += notas1

print("Digite a nota 2 de cada um dos alunos")
for j in range(0, n):
    notas2 = float(input(""))
    p2.append(notas2)
    soma2 += notas2

media1 = soma/n
media2 = soma2/n

print(f"A média da turma na prova 1 é {media1}")
print(f"A média da turma na prova 2 é {media2}")

if media1 > media2:
    print("A turma obteve maior média na prova 1")
else:
    print("A turma obteve maior média na prova 2")
