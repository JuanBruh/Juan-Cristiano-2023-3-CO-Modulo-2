import random

from dino_runner.components.obstacles.obstacle import obstacle
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS


class cactus (obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)   
        super().__init__(image, self.type)
        if SMALL_CACTUS:
           self.rect.y = 325 
        elif LARGE_CACTUS:
            self.rect.y = 360
        
        