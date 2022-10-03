herois = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]
herois.append("Homem-Aranha")
print(herois)

if "Thor" in herois:
    print("Thor está na posição ", herois.index("Thor"))

herois.remove("Homem de Ferro")
herois.remove("Viúva Negra")
print(herois)