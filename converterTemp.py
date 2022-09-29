
def menu():
    while True:
        resposta = int(input("Digite (1) se deseja converter Celsius para Farenheit ou (2) se quer converter Farenheit para Celsius: "))
        if resposta == 1:
            c = float(input("temperatura em Celsius: "))
            CtoF()
        elif resposta == 2:
            f = float(input("temperatura em Celsius: "))
            FtoC()
        else:
            print("opção inválida!")

def CtoF(c):
    f = (c*9/5) + 32
    return f

def FtoC(f):
    c = (f-32)*5/9
    return c