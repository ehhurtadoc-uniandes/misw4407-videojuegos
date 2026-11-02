import pygame


class CScreenShake:
    def __init__(self, shake_info: dict) -> None:
        self.intensity = shake_info["intensity"]
        self.duration = shake_info["duration"]
        self.timer = 0.0
        self.offset = pygame.Vector2(0, 0)
