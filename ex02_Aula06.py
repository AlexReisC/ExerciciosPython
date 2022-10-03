positivos = ()
while True:
    p = int(input("Digite números positivos: "))
    if p > 0:
        positivos = positivos + tuple([p])
    else:
        break

x = int(input("Digite o número que deseja verificar: "))
if x in positivos:
    print(f"{x} está na tupla.")
else:
    print(f"{x} não está na tupla.")
print(positivos)