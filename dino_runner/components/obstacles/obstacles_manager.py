import pygame
import random

from dino_runner.components.obstacles.bird import bird
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self, oType):
        if oType == 0:
            obstacle = cactus(SMALL_CACTUS)
            return obstacle
        elif oType == 1:
            obstacle = cactus(LARGE_CACTUS)
            return obstacle
        elif oType == 2:
            obstacle = bird()
            return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            oType = random.randint(0,2)
            obstacle = self.generate_obstacle(oType)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(2000)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)