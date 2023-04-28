from dino_runner.components.obstacles.obstacle import obstacle


class cactus (obstacle):
    def __init__(self, image):
        self.type = random.randit(0, 2)   
        super().__init__(image, self.type)  
        self.rect.y = 325 