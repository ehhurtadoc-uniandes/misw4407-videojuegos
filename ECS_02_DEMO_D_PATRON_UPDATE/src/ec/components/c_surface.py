from typing import final, override

import pygame

from src.ec.Component import Component
from src.ec.components.c_transform import CTransform


@final
class CSurface(Component):
    def __init__(self, size: pygame.Vector2, color: pygame.Color, screen: pygame.Surface):
        super().__init__()

        self.surf: pygame.Surface = pygame.Surface(size)
        self.surf.fill(color)

        self._screen: pygame.Surface = screen
        self._transform: CTransform | None = None

    @override
    def start(self) -> None:
        self._transform = self.game_object.get_component(CTransform)

    @override
    def draw(self):
        if self._transform is None:
            return
        self._screen.blit(self.surf, self._transform.position)
