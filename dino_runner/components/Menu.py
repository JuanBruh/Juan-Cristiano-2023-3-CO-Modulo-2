import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_CREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_CREEN_WIDTH = SCREEN_WIDTH // 2
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_CREEN_WIDTH, self.HALF_CREEN_HEIGHT)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False



