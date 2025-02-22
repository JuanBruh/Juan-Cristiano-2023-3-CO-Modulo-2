import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.skate import Skate
from dino_runner.utils.constants import SHIELD_SOUND, SKATE_SOUND


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
        self.duration = random.randint(3, 5)

    def generate_power_up(self, power_up_tye):
        if power_up_tye == 0:
            power_up = Shield()
            SHIELD_SOUND.play()
            return power_up
        elif power_up_tye ==1:
            power_up = Skate()
            SKATE_SOUND.play()
            return power_up
        
    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            power_up_type = random.randint(0,1)
            power_up = self.generate_power_up(power_up_type)
            self.when_appears += random.randint(100, 200)
            self.power_ups.append(power_up)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration* 1000)
                self.power_ups.remove(power_up)

            
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)

    