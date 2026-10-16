from typing import override

import pygame

from src.ent.entities.transform import Transform


class TransformMove(Transform):
    def __init__(self, pos: pygame.Vector2, vel: pygame.Vector2):
        super().__init__(pos)
        self.position: pygame.Vector2 = pos
        self.velocity: pygame.Vector2 = vel

    @override
    def update(self, delta_time: float) -> None:
        super().update(delta_time)

        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time
