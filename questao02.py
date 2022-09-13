lista = []
i = 0
n = int(input("Digite um número: "))

while n > 0:
    n = int(input("Digite um número: "))
    if n > 0:
        lista.append(n)

x = int(input("\nQual número quer verificar? "))
if x in lista:
    print(f"{x} está na lista")
else:
    print(f"{x} não está na lista")
