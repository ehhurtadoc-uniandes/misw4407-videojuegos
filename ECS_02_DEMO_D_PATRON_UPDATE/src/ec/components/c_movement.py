from typing import final, override

import pygame

from src.ec.Component import Component
from src.ec.components.c_transform import CTransform


@final
class CMovement(Component):
    def __init__(self, velocity: pygame.Vector2) -> None:
        super().__init__()
        self.velocity: pygame.Vector2 = velocity
        self._transform: CTransform | None = None

    @override
    def start(self) -> None:
        self._transform = self.game_object.get_component(CTransform)

    @override
    def update(self, delta_time: float) -> None:
        if self._transform is None:
            return
        self._transform.position.x += self.velocity.x * delta_time
        self._transform.position.y += self.velocity.y * delta_time
