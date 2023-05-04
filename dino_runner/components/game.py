import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE

from dino_runner.components.dino import Dinosaur
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.Menu import Menu
from dino_runner.components.counter import Counter

class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.death_count = Counter()
        self.score = Counter()
        self.highest_Score = Counter()
    
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
        self.score.update()
        self.update_game_speed()
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

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

        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0:
            self.menu.draw(self.screen, 'Welcome. Press any key to start.')
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Game over. Press any key to restart.')
            self.menu.draw(self.screen, f'Your Score: {self.score.count}', half_screen_width, 350)
            self.menu.draw(self.screen, f'Highest score: {self.highest_Score.count}', half_screen_width, 400)
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 450)


        self.screen.blit(ICON, (half_screen_heigth - 50 , half_screen_width - 150))
        self.menu.update(self)


    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 250:
            self.game_speed += 5

    def update_highest_score(self):
        if self.score.count > self.highest_Score.count:
            self.highest_Score.set_count(self.score.count)



    def reset_all(self):
        self.obstacle_manager.reset()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
    


  