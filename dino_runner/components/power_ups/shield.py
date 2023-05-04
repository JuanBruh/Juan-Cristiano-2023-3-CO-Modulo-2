from dino_runner.components.power_ups import power_up
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE


class Shiel(power_up):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)