import time
import pygame
from pygame.locals import * #está importando coisas necessárias para lidar com gráficos

# Inicialização do Pygame
pygame.init()#inicializa o programa no pygame

# Definindo as dimensões da janela
largura = 800
altura = 200
tamanho_tecla = 60

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Criando a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("midia Simples")

# Carregando sons das teclas
sons = {
    K_a: pygame.mixer.Sound("midia/do.wav"),
    K_s: pygame.mixer.Sound("midia/re.wav"),
    K_d: pygame.mixer.Sound("midia/mi.wav"),
    K_f: pygame.mixer.Sound("midia/fa.wav"),
    K_g: pygame.mixer.Sound("midia/sol.wav"),
    K_h: pygame.mixer.Sound("midia/la.wav"),
    K_j: pygame.mixer.Sound("midia/si.wav"),
   
}
do = pygame.mixer.Sound("midia/do.wav")
re = pygame.mixer.Sound("midia/re.wav")
mi = pygame.mixer.Sound("midia/mi.wav")
fa = pygame.mixer.Sound("midia/fa.wav")
sol = pygame.mixer.Sound("midia/sol.wav")
la = pygame.mixer.Sound("midia/la.wav")
si = pygame.mixer.Sound("midia/si.wav")

def roda_musica():
    mi.play()
    time.sleep(0.5)
    fa.play()
    time.sleep(0.1)
    sol.play()
    time.sleep(0.1)
    do.play()
    time.sleep(1.0)
    si.play()
    time.sleep(0.5)
    la.play()
    time.sleep(0.5)
    sol.play()
    time.sleep(0.5)
    mi.play()
    time.sleep(0.5)
    do.play()
    

roda_musica()
# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if evento.key in sons:
                sons[evento.key].play()

    # Desenhar o midia na tela
    janela.fill(branco)
    for i, (tecla, som) in enumerate(sons.items()):
        pygame.draw.rect(janela, preto if i % 2 == 0 else branco, (i * tamanho_tecla, 0, tamanho_tecla, altura))
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()