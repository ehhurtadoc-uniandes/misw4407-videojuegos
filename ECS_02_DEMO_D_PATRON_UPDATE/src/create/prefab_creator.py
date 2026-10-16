import pygame

from src.ec.components.c_bounce import CBounce
from src.ec.components.c_movement import CMovement
from src.ec.components.c_surface import CSurface
from src.ec.components.c_transform import CTransform
from src.ec.GameObjectManager import GameObjectManager


def create_square(
    game_object_manager: GameObjectManager,
    size: pygame.Vector2,
    pos: pygame.Vector2,
    vel: pygame.Vector2,
    col: pygame.Color,
    screen: pygame.Surface,
    screen_rect: pygame.FRect,
):
    go = game_object_manager.create_game_object()
    go.add_component(CTransform(pos))
    go.add_component(CMovement(vel))
    go.add_component(CSurface(size, col, screen))
    go.add_component(CBounce(screen_rect))
