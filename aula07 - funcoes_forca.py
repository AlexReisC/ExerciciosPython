import random

#print(random.randrange(1, len(palavras)))
#print(palavras[random.randrange(1, len(palavras))])
def jogar():
    palavra_secreta = carrega_palavra_secreta()

    letras_certas = inicializa_letras()

    #var = 0
    #while var < len(palavra_secreta):
    #    letras_certas.append('_')
    #    var += 1
    #print(letras_certas)
    acertou = False
    enforcou = False
    tentativas = 1

    while(not enforcou and not acertou):
        chute = input("Digite uma letra")
        chute = chute.lower()
        chute = chute.strip()



        if chute in palavra_secreta:
                posicao = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_certas[posicao] = letra
                        print("Encontrei a letra {} na posição {}".format(chute, posicao))
                        if letras_certas.count("_") == 0:
                            print("Acertou A palavra secreta é {}".format(palavra_secreta))
                            acertou = True
                    posicao += 1
        else:
            if (tentativas >= len(palavra_secreta)):
                enforcou = True
                print("Você acertou apenas as letras ", letras_certas)
                print("Enforcou! A palavra secreta é {}".format(palavra_secreta))

        print("Tentativas restantes", len(palavra_secreta) - tentativas)
        print(letras_certas)
        tentativas += 1

def carrega_palavra_secreta():
    palavras = ['Monitor', 'Teclado', 'Mouse', 'Impressora', 'Notebook', 'Scanner']
    palavra_secreta = palavras[random.randrange(0, len(palavras))].lower()
    print(palavra_secreta)
    return palavra_secreta

def inicializa_letras(palavra_secreta):
    letras_certas = []
    for letra in palavra_secreta:
        print(letra)
        letras_certas.append('_')
    print(letras_certas)
    return letras_certas


if __name__ == '__main__':
    jogar()
