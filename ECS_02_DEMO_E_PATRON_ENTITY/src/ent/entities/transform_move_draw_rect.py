from typing import override

import pygame
from pygame.math import Vector2

from src.ent.entities.transform_move import TransformMove


class TransformMoveDrawRect(TransformMove):
    def __init__(self, pos: Vector2, vel: pygame.Vector2, size: pygame.Vector2, col: pygame.Color):
        super().__init__(pos, vel)
        self.surface: pygame.Surface = pygame.Surface(size)
        self.surface.fill(col)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
        screen.blit(self.surface, self.position)
