# criar dicionario vazio
dicionario = dict([])
print(type(dicionario))
print(dicionario)


#criar dicionario
professores = {'Dorgival' : 33, 'Flavio': 37, 'Marcos' : 30}
print(type(professores))
print(professores)

print("\n")
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

#acessando valores
print(eng2sp['two'])
print(eng2sp.get('three'))

#função len: retorna numero de pares
print(len(eng2sp))

#in verifica se algo é chave
if 'one' in eng2sp:
    print("É chave")
elif 'uno' in eng2sp:
    print("chave")

#values verifica retorna uma coleção de valores
valores = eng2sp.values()
if 'uno' in valores:
    print("É valor")

#adicionar novos valores a um dicionario
eng2sp['four'] = 'cuatro'
print(eng2sp)

#exemplo de agenda telefonica
agenda = {"Maria":[99887766, 99887755], "Pedro":[92345678], "Joaquim":[99887711, 99665533]}
print(agenda)

telMaria = agenda["Maria"]
print(telMaria)
print(agenda["Maria"])

#alterar valor
agenda["Pedro"] = [87654433]
print(agenda)

#acrescentar novos valores: basta fazer atribuição a uma chave não existente
agenda["Teresa"] = [65443322]
print(agenda)

#remover um valor e chave
numeracao = eng2sp.pop('four')
print(numeracao)

del  eng2sp['one']
print(eng2sp)
#popitem remove o ultimo par e retorna-os
print(eng2sp.popitem())

#update atualiza um dicionario
dic_a = {"A": "Avião", "B": "Barco"}
dic_b = {"B": "Balão", "C": "Carro"}
dic_a.update(dic_b)
print(dic_a)

#keys retorna uma estrutura com as chaves do dicionário, que pode ser convertida para uma lista
lugar = {"Lat": -22.817087, "Long": -47.069750}
print(lugar.keys())
print(list(lugar.keys()))

#items retorna uma estrutura que pode ser convertida para uma lista de tuplas, onde cada tupla é composta pelo par (chave, valor)
lugar = {"Lat": -22.817087, "Long": -47.069750}
print(lugar.items())
print(list(lugar.items()))

#iteração em uma lista de chaves usando o método keys
dic = {"A": "Abacate",  "B": "Banana", "C": "Caqui" }
for letra in dic.keys():
    print("Letra: ", letra)

#Podemos iterar sobre uma lista de valores utilizando o método values.
dic = {"A": "Abacate",  "B": "Banana", "C": "Caqui" }
for letra in dic.values():
    print("Letra:", letra)

#Podemos também iterar sobre uma lista de tuplas contendo as chaves e os valores utilizando o método items.
dic = { "A": "Abacate", "B": "Banana",  "C": "Caqui" }
for (letra, fruta) in dic.items():
    print("Fruta com Letra", letra, ":", fruta)

#copiar dicionarios
dic_a = {"Nome": "João", "Idade": 18}
print(dic_a)  # {'Nome': 'João', 'Idade': 18}
dic_b = dic_a.copy()
#dic_b["Nome"] = "Maria"
print(dic_b)
