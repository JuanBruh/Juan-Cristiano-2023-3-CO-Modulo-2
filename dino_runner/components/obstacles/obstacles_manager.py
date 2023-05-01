import pygame
import random

from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self, oType):
        self.oType = oType[cactus(SMALL_CACTUS),
                           cactus(LARGE_CACTUS)]
        
        obstacle = self.oType

        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            self.oType = random.randint(0,2)
            obstacle = self.generate_obstacle(self.oType)
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