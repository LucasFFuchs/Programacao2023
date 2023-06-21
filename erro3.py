#Erro na linha 77

import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

# Definição do tamanho da tela
largura = 400
altura = 400
tamanho_quadrado = largura // 3

# Criação da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Velha")

# Matriz para guardar o estado do tabuleiro
tabuleiro = [['', '', ''],
             ['', '', ''],
             ['', '', '']]

# Variável para controlar o turno do jogador
jogador_atual = 'X'

# Função para desenhar o tabuleiro na tela
def desenhar_tabuleiro():
    tela.fill(BRANCO)
    pygame.draw.line(tela, PRETO, (tamanho_quadrado, 0), (tamanho_quadrado, altura), 2)
    pygame.draw.line(tela, PRETO, (2 * tamanho_quadrado, 0), (2 * tamanho_quadrado, altura), 2)
    pygame.draw.line(tela, PRETO, (0, tamanho_quadrado), (largura, tamanho_quadrado), 2)
    pygame.draw.line(tela, PRETO, (0, 2 * tamanho_quadrado), (largura, 2 * tamanho_quadrado), 2)

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 'X':
                pygame.draw.line(tela, PRETO, (coluna * tamanho_quadrado + 15, linha * tamanho_quadrado + 15),
                                 ((coluna + 1) * tamanho_quadrado - 15, (linha + 1) * tamanho_quadrado - 15), 3)
                pygame.draw.line(tela, PRETO, ((coluna + 1) * tamanho_quadrado - 15, linha * tamanho_quadrado + 15),
                                 (coluna * tamanho_quadrado + 15, (linha + 1) * tamanho_quadrado - 15), 3)
            elif tabuleiro[linha][coluna] == 'O':
                pygame.draw.circle(tela, AZUL, (coluna * tamanho_quadrado + tamanho_quadrado // 2,
                                                linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 15, 3)

# Função para verificar se alguém ganhou o jogo
def verificar_vitoria(jogador):
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == jogador:
            return True
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

# Função principal do jogo
def jogo_da_velha():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and not verificar_vitoria('X') and not verificar_vitoria('O'):
                posicao = pygame.mouse.get_pos()
                coluna = posicao[0] // tamanho_quadrado
                linha = posicao[1] // tamanho_quadrado

                if tabuleiro[linha][coluna] == '':
                    tabuleiro[linha][coluna] = jogador_atual #O programa tenta de novo puxar uma variavel dentro de uma função, sendo que ela não está definida como global
                    if jogador_atual == 'X':
                        jogador_atual = 'O'
                    else:
                        jogador_atual = 'X'

        desenhar_tabuleiro()
        if verificar_vitoria('X'):
            pygame.display.set_caption("Jogo da Velha - Jogador X venceu!")
        elif verificar_vitoria('O'):
            pygame.display.set_caption("Jogo da Velha - Jogador O venceu!")
        pygame.display.update()

# Inicialização do jogo
jogo_da_velha()
