import random

palavras = ["Carro", "Bola", "Aviao", "Escola", "Celular"]

palavra_secreta = palavras[random.randrange(0, len(palavras))].lower()

letras_certas = []
for letra in palavra_secreta:
    letras_certas.append("_")

print("_ " * len(palavra_secreta))
tentativas = len(palavra_secreta)

acertou = False
while tentativas > 0:
    palpite = input("Digite uma letra: ")
    palpite.lower().strip()
    if len(palpite) > 1:
        print("Digite apenas uma letra...")
    elif palpite in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if palpite == letra:
                letras_certas[posicao] = letra
                print("Encontrou a letra '{}' na posição {}" .format(letra, posicao))
                tentativas -= 1
            posicao += 1
        if letras_certas.count("_") == 0:
            print("Você acertou a palavra!!!")
            acertou = True
            break
    else:
        tentativas -=1

if tentativas == 0 and acertou == False:
    print("Você enforcou! E acertou estas {} letras" .format(letras_certas))
