#Erro linha 55

import pygame
import time

# Inicializando o Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definindo as dimensões da janela
largura_janela = 400
altura_janela = 300

# Criando a janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Cronômetro")

# Criando a fonte
fonte = pygame.font.Font(None, 50)

# Variáveis do cronômetro
tempo_inicial = None
tempo_passado = 0
cronometro_ligado = False

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        # Verificando se a tecla espaço foi pressionada
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            if cronometro_ligado:
                cronometro_ligado = False
                tempo_passado = time.time() - tempo_inicial
            else:
                cronometro_ligado = True
                tempo_inicial = time.time()

    # Preenchendo a janela com a cor preta
    janela.fill(PRETO)

    # Calculando o tempo atual do cronômetro
    if cronometro_ligado:
        tempo_atual = time.time() - tempo_inicial + tempo_passado
    else:
        tempo_atual = tempo_passado

    # Convertendo o tempo para uma string formatada (mm:ss.ms)
    tempo_string = time.strftime("%M:%S.%f", time.gmtime(tempo_atual))[0:7] # %f não funciona corretamente em certas versões do python/pygame

    # Renderizando o texto do cronômetro na janela
    texto = fonte.render(tempo_string, True, BRANCO)
    janela.blit(texto, (150, 120))

    # Atualizando a janela
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()
