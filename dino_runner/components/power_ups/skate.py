from dino_runner.components.power_ups.power_up import Power_up
from dino_runner.utils.constants import SKATE, SKATE_TYPE


class Skate(Power_up):
    def __init__(self):
        super().__init__(SKATE, SKATE_TYPE)