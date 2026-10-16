import pygame

from src.ent.entity import Entity


class Transform(Entity):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.position: pygame.Vector2 = pos
