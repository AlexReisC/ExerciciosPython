import pygame
amarelo = (255, 255, 0)
preto = (0, 0, 0)
raio = 50

pygame.init()
tela = pygame.display.set_mode((640, 480), 0)
x = 10
velocidade_x = 0.1
y = 10
velocidade_y = 0.5

while True:
    tela.fill(preto)
    x = x + velocidade_x
    y = y + velocidade_y
    pygame.draw.circle(tela, amarelo, (int(x), int(y)), raio, 0)
    pygame.display.update()
    if (x + raio) > 640:
        velocidade_x = -0.1
    if (x - raio) < 0:
        velocidade_x = 0.1
    if (y + raio) > 480:
        velocidade_y = -0.5
    if (y - raio) < 0:
        velocidade_y = 0.5
    for E in pygame.event.get():
        if E.type == pygame.QUIT:
            exit()
