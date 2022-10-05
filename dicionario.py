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

