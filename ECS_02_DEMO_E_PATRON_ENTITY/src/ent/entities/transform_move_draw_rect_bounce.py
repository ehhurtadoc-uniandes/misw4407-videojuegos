from typing import override

import pygame

from src.ent.entities.transform_move_draw_rect import TransformMoveDrawRect


class TransformMoveDrawRectBounce(TransformMoveDrawRect):
    def __init__(
        self,
        pos: pygame.Vector2,
        vel: pygame.Vector2,
        size: pygame.Vector2,
        col: pygame.Color,
        screen_rect: pygame.FRect,
    ):
        super().__init__(pos, vel, size, col)
        self.screen_rect: pygame.FRect = screen_rect

    @override
    def update(self, delta_time: float) -> None:
        super().update(delta_time)

        cuad_rect = self.surface.get_frect(topleft=self.position)
        if cuad_rect.left < 0 or cuad_rect.right > self.screen_rect.width:
            self.velocity.x *= -1
            cuad_rect.clamp_ip(self.screen_rect)
            self.position.x = cuad_rect.x

        if cuad_rect.top < 0 or cuad_rect.bottom > self.screen_rect.height:
            self.velocity.y *= -1
            cuad_rect.clamp_ip(self.screen_rect)
            self.position.y = cuad_rect.y
