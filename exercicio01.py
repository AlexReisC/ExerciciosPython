#nome = input("Qual o nome do arquivo? ")
arq = open("arquivoNovo.txt", "w")
arq.write("Mussum Ipsum, cacilds vidis litro abertis. Nullam volutpat risus nec leo commodo, ut interdum diam laoreet. Sed non consequat odio.Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis.Leite de capivaris, leite de mula manquis sem cabeça.Delegadis gente finis, bibendum egestas augue arcu ut est.\nCasamentiss faiz malandris se pirulitá.Tá deprimidis, eu conheço uma cachacis que pode alegrar sua vidis.Diuretics paradis num copo é motivis de denguis.Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.\nInteragi no mé, cursus quis, vehicula ac nisi.Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.Não sou faixa preta cumpadi, sou preto inteiris, inteiris.Diuretics paradis num copo é motivis de denguis.")
arq.close()
arq = open("arquivoNovo.txt", "r")
for linha in arq:
    print("Linha do arquivo: {}" .format(linha))
""" conteudo = arq.read()
print(conteudo)
arq.close() """