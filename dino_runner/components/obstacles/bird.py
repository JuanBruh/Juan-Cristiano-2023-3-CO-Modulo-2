import random

from dino_runner.components.obstacles.obstacle import obstacle

from dino_runner.utils.constants import BIRD



class bird (obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2) 
        super().__init__(image, self.type)
        self.image = BIRD
        self.step_index = 0
        if self.type == 0:
            self.rect.y = 325 
        elif self.type == 1:
            self.rect.y = 300
        elif self.type == 2:
            self.rect.y = 250
         

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

    def update(self):
        if self.step_index >= 10:
            self.step_index = 0