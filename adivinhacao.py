from random import randint

numero_secreto = randint(1, 100)
pontos_jogador = 1000

dific = 0
while dific < 1 or dific > 3:
    dific = int(input("Selecione a dificuldade: (1)Fácil (2)Médio (3)Difícil: "))

if dific == 1:
    tentativas = 20
elif dific == 2:
    tentativas = 10
else:
    tentativas = 5

while tentativas > 0:
    print("Você tem {} tentativas" .format(tentativas))
    chute_jogador = int(input("Digite um número: "))
    if chute_jogador < 1 or chute_jogador > 100:
        print("Digite um número entre 1 e 100...")
        tentativas -=1
    else:
        if chute_jogador < numero_secreto:
            print("Você errou! O seu número é menor que o número secreto.")
            pontos_jogador = pontos_jogador - (numero_secreto - chute_jogador)
            tentativas -= 1
        elif chute_jogador > numero_secreto:
            print("Você errou! O seu número é maior que o número secreto.")
            pontos_jogador = pontos_jogador - (chute_jogador - numero_secreto)
            tentativas -= 1
        else:
            print("Você Acertou! Parabéns!")
            break

if tentativas == 0:
    print("GAME OVER! VOCÊ PERDEU!")
    print("o número era o {}" .format(numero_secreto))
print("Pontos do jogador: {}" .format(pontos_jogador))
