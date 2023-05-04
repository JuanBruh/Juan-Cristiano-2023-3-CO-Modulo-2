import pygame
import random

from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.Cactus import Cactus
from dino_runner.utils.constants import DEAD_SOUND
from dino_runner.utils.constants import SHIELD_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
            return obstacle
        elif obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
            return obstacle
        elif obstacle_type == 2:
            obstacle = Bird()
            return obstacle
            

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0,2)
            obstacle = self.generate_obstacle(obstacle_type)           
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    DEAD_SOUND.play()
                    game.player.dead()
                    pygame.time.delay(2000)
                    game.death_count.update()
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []