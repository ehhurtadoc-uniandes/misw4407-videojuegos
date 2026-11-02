import pygame


class CHudBar:
    def __init__(self, full_width: int, color_ready: pygame.Color, color_active: pygame.Color,
                 color_cooldown: pygame.Color) -> None:
        self.full_width = full_width
        self.color_ready = color_ready
        self.color_active = color_active
        self.color_cooldown = color_cooldown
