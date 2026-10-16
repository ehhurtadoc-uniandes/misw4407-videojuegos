from typing import final, override

import pygame

from src.ec.Component import Component
from src.ec.components.c_movement import CMovement
from src.ec.components.c_surface import CSurface
from src.ec.components.c_transform import CTransform


@final
class CBounce(Component):
    def __init__(self, screen_rect: pygame.FRect) -> None:
        super().__init__()
        self._screen_rect: pygame.FRect = screen_rect
        self._transform: CTransform | None = None
        self._movement: CMovement | None = None
        self._surface: CSurface | None = None

    @override
    def start(self) -> None:
        self._transform = self.game_object.get_component(CTransform)
        self._movement = self.game_object.get_component(CMovement)
        self._surface = self.game_object.get_component(CSurface)

    @override
    def update(self, delta_time: float) -> None:
        if self._transform is None or self._movement is None or self._surface is None:
            return

        cuad_rect = self._surface.surf.get_frect(topleft=self._transform.position)
        if cuad_rect.left < 0 or cuad_rect.right > self._screen_rect.width:
            self._movement.velocity.x *= -1
            cuad_rect.clamp_ip(self._screen_rect)
            self._transform.position.x = cuad_rect.x

        if cuad_rect.top < 0 or cuad_rect.bottom > self._screen_rect.height:
            self._movement.velocity.y *= -1
            cuad_rect.clamp_ip(self._screen_rect)
            self._transform.position.y = cuad_rect.y
