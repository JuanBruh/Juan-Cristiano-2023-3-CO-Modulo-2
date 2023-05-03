import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE

from dino_runner.components.dino import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start...', self.screen)
        self.death_count = 0
        self.score = 0
    
    def execute(self):
        self.runing = True
        while self.runing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_all()
        self.obstacle_manager.reset()
        self.player.reset_dino()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH //2

        self.menu.reset_screen_color()

        font = pygame.font.Font(FONT_STYLE, 30)

        if self.death_count > 0:
            self.menu.update_message('Game Over. Press any key to restart.')
            your_score = font.render(f'Your Score: {self.score}', True, (0, 0, 0))
            your_score_rect = total_deaths.get_rect()
            your_score_rect.center = (half_screen_heigth + 100, half_screen_width - 200)
            self.screen.blit(your_score, your_score_rect) 
            total_deaths = font.render(f'Total Deaths: {self.death_count}', True, (0, 0, 0))
            total_deaths_rect = total_deaths.get_rect()
            total_deaths_rect.center = (half_screen_heigth + 300, half_screen_width - 200)
            self.screen.blit(total_deaths, total_deaths_rect) 
            

        self.menu.draw(self.screen)

        self.screen.blit(ICON, half_screen_heigth - 50 , half_screen_width - 150)

        

        self.menu.update(self)
    
    def update_score(self):
        self.score += 1

        if self.score % 100 and self.game_speed < 250:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect) 

    def reset_all(self):
        self.score = 0
        self.game_speed = 20



  