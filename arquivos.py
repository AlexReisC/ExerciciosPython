""" print("Arquivo 1:")
arquivo = "dados\net.txt"
print(arquivo)

print("Arquivo 2:")
arquivo2 = "dados\\net.txt"
print(arquivo2)

print("Arquivo 3:")
arquivo3 = "dados/net.txt"
print(arquivo3)

print("Arquivo 4:")
import os
arquivo4 = os.path.join("dados","net.txt")
print(arquivo4) """

arquivo = open("arquivo.txt", "w")
arquivo.write("O texto que nós queremos escrever no arquivo!")
arquivo.close()
print(arquivo)

arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)

print("="*40)
with open("arquivo.txt", "r") as f:
    dados = f.read(30)
    print(dados)
    dados = f.read()

print("Dados com with: ", dados)

