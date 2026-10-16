import pygame

from src.ent.entities.transform_move_draw_rect_bounce import TransformMoveDrawRectBounce
from src.ent.entity_manager import EntityManager


def create_square(
    entity_manager: EntityManager,
    size: pygame.Vector2,
    pos: pygame.Vector2,
    vel: pygame.Vector2,
    col: pygame.Color,
    screen_rect: pygame.FRect,
) -> None:
    entity_manager.add_entity(
        TransformMoveDrawRectBounce(pos=pos, vel=vel, size=size, col=col, screen_rect=screen_rect)
    )
