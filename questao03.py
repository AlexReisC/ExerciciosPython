lista = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]
lista.append("Homem-Aranha")

for i in range(0, len(lista)):
    if "Thor" in lista:
        print("Thor está na posição", lista.index("Thor"))
        break

del(lista[0])
del(lista[3])
print(lista)
