#TUPLAS
#Declaração implicita
t1 = ("a")
t2 = ("a", )
print(type(t1))
print(type(t2))
#Declaração explicita
t3 = tuple(["b", 23324])
t4 = tuple(["cc0016", 12])
print(t3)
print(t4)

#Verificando se um elemento está em uma tupla
top3 = ("The Boys", "The Big Bang Theory", "Supernatural")
print("Game of Thrones" in top3)
print("The Boys" in top3)

#Concatenando tuplas
a = (1, 2)
b = (3, 4)
c = (5, 6)
print(a + b + c)
print(c + b + a)
print(b + c + a)

#Obtendo posição de um elemento
cinema = ("Sony", "Disney", "DreamWorks", "Warner")
print(cinema.index("Disney"))
#Evitando erro
if "Pixar" in cinema:
    print(cinema.index("Pixar"))
else:
    print("Pixar não está na tupla")

#Imprimindo todos os elementos
for estudio in cinema:
    print(estudio)

#Criando uma tupla de forma iterativa
n =int(input("Quantos números serão lidos?"))
tupla = ()
for i in range(n):
   x = int(input("Entre com um número:"))
   tupla = tupla + tuple([x])
print(tupla)

print("="*30)
#DICIONARIO
