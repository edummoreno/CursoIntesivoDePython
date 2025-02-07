import sys
import pygame

from settings import Settings

# Classe:
#   - 'AlienInvasion' é uma classe que serve de molde para o jogo.
#     Ela define os atributos (como a tela do jogo) e os métodos (como inicialização e loop principal)
#     que gerenciam os ativos e o comportamento do jogo.
class AlienInvasion:
    # Classe geral para gerenciar ativos e comportamento do jogo

    # Método __init__ (construtor):
    #   - É executado automaticamente quando um objeto da classe é criado (instanciação).
    #   - Inicializa os atributos do objeto, como a janela do jogo.
    def __init__(self):
        # Inicializa todos os módulos do Pygame, preparando o ambiente para o jogo."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # seta as configurações?
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Redesenha a teka durante cada passagem pelo loop.
        self.screen.fill(self.settings.bg_color)

        # Atributo:
        #   - 'self.screen' armazena a janela do jogo, criada com dimensões 1200x800 pixels.
        self.screen = pygame.display.set_mode((1200, 800))
        # Configura o título da janela do jogo.
        pygame.display.set_caption("Alien Invasion")
        # Definindo uma Cor
        self.bg_color = (64, 224, 208)

    # Método run_game:
    #   - Define o loop principal do jogo, que mantém o jogo em execução.
    #   - Dentro desse loop, são tratados os eventos (como cliques e pressionamentos de tecla)
    #     e atualizada a tela para exibir os desenhos mais recentes.
    def run_game(self):
        # Inicia o loop principal do jogo
        while True:
            # Observa eventos de teclado e mouse (por exemplo, fechar a janela)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # Encerra o programa quando o usuário fecha a janela

            # Atualiza a tela para que as alterações sejam visíveis ao usuário
            pygame.display.flip()
            self.clock.tick(60)

            # Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.bg_color)

# Bloco principal:
#   - Verifica se este script está sendo executado diretamente e não importado como módulo.
if __name__ == '__main__':
    # Instanciação:
    #   - Cria um objeto 'ai' da classe 'AlienInvasion'.
    #     Esse objeto possui todos os atributos e métodos definidos na classe.
    ai = AlienInvasion()
    # Chamada de método:
    #   - Executa o método 'run_game()' do objeto 'ai', iniciando o loop principal do jogo.
    ai.run_game()
