import pygame


class CHudText:
    def __init__(self, font: pygame.font.Font, color: pygame.Color, center_x: int,
                 text: str, text_active: str) -> None:
        self.font = font
        self.color = color
        self.center_x = center_x
        self.text_ready = text
        self.text_active = text_active
        self.current_text = text
