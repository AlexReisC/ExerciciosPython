n = int(input("Digite um número: "))
tupla = ()
for i in range(n):
    m = int(input("Adicione um número: "))
    tupla = tupla + tuple([m])

x = int(input("Qual número quer verificar? "))
if x in tupla:
    print(f"{x} está na tupla")
else:
    print(f"{x} não está na tupla")

print(tupla)