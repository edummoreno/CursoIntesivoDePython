import pygame

class nave:
    # Classe para cuidar da espaçonave


    def __init__(self, ai_game):
        # Inicializa a espaçonave e defina sua posição Inicial
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagem/nave.bmp')
        self.rect  = self.image.get_rect()

        #Começa cada esaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Desenha a espaçonave em sua localização atual
        self.screen.blit(self.image, self.rect)