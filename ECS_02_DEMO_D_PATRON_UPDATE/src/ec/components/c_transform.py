from typing import final

import pygame

from src.ec.Component import Component


@final
class CTransform(Component):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.position: pygame.Vector2 = position
